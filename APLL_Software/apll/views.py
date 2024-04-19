from django.shortcuts import render
from .models import Carro


# Create your views here.

def home(request):
    return render(request, 'home.html')


def filter_carros(request):
    marcas = Carro.objects.values_list('Marca', flat=True).distinct()
    marca_selected = request.GET.get('marca')
    linea_selected = request.GET.get('linea')


    queryset = Carro.objects.all()
    lineas = Carro.objects.none()
    modelos = Carro.objects.none()

    if marca_selected:
        queryset = queryset.filter(Marca=marca_selected)
        lineas = Carro.objects.filter(Marca=marca_selected).values_list('Linea', flat=True).distinct()
    if linea_selected:
        queryset = queryset.filter(Linea=linea_selected)
        modelos = Carro.objects.filter(Marca=marca_selected, Linea=linea_selected).values_list('Modelo', flat=True).distinct()

    context = {
        'marcas': marcas,
        'lineas': lineas,
        'modelos': modelos,
        'marca_selected': marca_selected,
        'linea_selected': linea_selected,
        'carros': queryset
    }
    return render(request, 'pruebarep.html', context)
