from django.db import models

# Create your models here.

class Service(models.Model):
    title= models.CharField(max_length=200, verbose_name='Titulo')
    subtitle= models.CharField(max_length=200, verbose_name='Subtitulo')
    content= models.TextField(verbose_name='Contenido')
    image= models.ImageField(upload_to='services/', height_field=None, width_field=None, max_length=None, verbose_name='Imagen')
    created= models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated= models.DateTimeField(auto_now=True, verbose_name='Modificado')
    
    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['created']
        
    def __str__(self):
        return self.title