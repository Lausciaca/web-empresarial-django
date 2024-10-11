from django.shortcuts import render
from . import models

# Create your views here.
def services(request):
    return render(request, 'services/services.html', {'servicios': models.Service.objects.all})