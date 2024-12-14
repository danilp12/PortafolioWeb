# forms.py
from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(label='Tu Email', max_length=100)
    subject = forms.CharField(label='Asunto', max_length=100)
    message = forms.CharField(label='Mensaje', widget=forms.Textarea)
