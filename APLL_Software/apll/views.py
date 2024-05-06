from django.shortcuts import render
from .models import Carro
from django.shortcuts import redirect

# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')


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



def redirect_by_group(request):
    if request.user.is_authenticated:
        user_groups = request.user.groups.all()
        if user_groups.filter(name='Admin').exists():
            # Redireccionar a Pagina ADMIN 
            return redirect('url_admin')
        elif user_groups.filter(name='Ventas').exists():
            # Redireccionar a pagina Ventas
            return redirect('url_ventas')
        else:
            # Redireciona a home
            return redirect('url_home')
    else:
        # Redirecciona a LOGIN
        return redirect('url_login')

