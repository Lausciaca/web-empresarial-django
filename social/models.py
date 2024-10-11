from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name='Nombre clave', unique=True, max_length=100)
    name = models.CharField(max_length=100, verbose_name='Nombre')
    url = models.URLField(max_length=200, verbose_name='Enlace', null=True, blank=True)
    created= models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated= models.DateTimeField(auto_now=True, verbose_name='Modificado')
    
    class Meta:
        verbose_name = 'link'
        verbose_name_plural = 'links'
        ordering = ['created']
        
    def __str__(self):
        return self.name