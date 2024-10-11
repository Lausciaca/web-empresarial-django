from django.contrib import admin
from .models import Service

# Register your models here.
# creamos una clase que permita gestionar el administrador del modelo
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    
    
# registramos el modelo en el administrador, pasando el modelo y el controlador
admin.site.register(Service, ServiceAdmin)