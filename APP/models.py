from django.db import models

# Create your models here.
class Certificado(models.Model):
    titulo = models.CharField(max_length=200)
    img = models.ImageField(upload_to="img/Certificados")
    def __str__(self):
        return self.titulo