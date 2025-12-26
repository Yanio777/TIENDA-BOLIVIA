from django.shortcuts import render
from .models import ProductoBoliviano

def tienda_inicio(request):
    productos = ProductoBoliviano.objects.all()
    return render(request, 'index.html', {'productos': productos})