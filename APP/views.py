from django.shortcuts import render
from .models import Certificado
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
import requests

# Create your views here.
def inicio(request):
    if request.session.get('header_animated', False):
        # Marcar como que se debe mostrar la animación
        request.session['header_animated'] = True
        show_animation = True
    else:
        # Si ya se ha mostrado, no mostrar la animación
        show_animation = False
    return render(request,"base.html",{'show_animation': show_animation})
def proyectos(request):
    url = 'https://api.github.com/users/danilp12/repos'
    response = requests.get(url)
    repositorios = response.json() if response.status_code == 200 else []
    
    # Ordenar los repositorios desde el último al primero
    repositorios = sorted(repositorios, key=lambda x: x['created_at'], reverse=True)
    
    return render(request, 'proyectos.html', {'repositorios': repositorios})
def sobremi(request):
    return render(request,"sobremi.html")

def certificados_list(request):
    certificados = Certificado.objects.all()
    return render(request, 'certificados_list.html', {'certificados': certificados})

def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Enviar el correo electrónico
            send_mail(
                subject,
                message,
                email,  # Desde el email del remitente
                [settings.EMAIL_HOST_USER],  # Email destino (puedes cambiarlo)
                fail_silently=False,
            )
            return render(request, 'inicio.html')  # Redirigir a una página de éxito
    else:
        form = ContactForm()

    return render(request, 'contacto.html', {'form': form})
def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
