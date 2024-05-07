from django.shortcuts import render
from .models import Carro
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from telnetlib import LOGOUT
from .models import Empleados
from .models import Carro
from .models import Repuestos
from .models import Inventario
from .models import Usuario
from .models import Cliente
from .models import Venta
from .models import Detalles_Venta
from .models import Comisiones
from .models import Departamentos
from .models import Pagos
from .models import Cotizacion
from .models import Cotizacion_Detalle
from .models import Compra_Carro
from .models import Compra_Repuesto
from .models import Proveedor
from .models import Bitacora_Alertas
from .models import Historial_Cambio
from .models import Cambios_Salarios

# Create your views here.

def home(request):
    return render(request, 'home.html')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or some other URL
            return redirect('home')  # Adjust the URL name as needed
        else:
            # Return an error message if authentication fails
            messages.error(request, 'Invalid username or password.')
    # If the request method is not POST or authentication fails, render the login page
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
    


@login_required
def menu_view(request):
    return render(request, 'menu.html')

def logout_view(request):
    LOGOUT(request)
    return redirect('login')

def vendedor_menu_view(request):
    return render(request, 'vendedor_menu.html')

def admin_menu_view(request):
    return render(request, 'admin_menu.html')

def contador_menu_view(request):
    return render(request, 'contador_menu.html')

def comprador_menu_view(request):
    return render(request, 'comprador_menu.html')

def lista_empleados(request):
    empleados = Empleados.objects.all()
    return render(request, 'empleado.html', {'empleados': empleados})

def lista_carros(request):
    carros = Carro.objects.all()
    return render(request, 'carros.html', {'carros': carros})

def lista_repuestos(request):
    repuestos = Repuestos.objects.all()
    return render(request, 'repuestos.html', {'repuestos': repuestos})

def lista_inventario(request):
    inventario = Inventario.objects.all()
    return render(request, 'inventario.html', {'inventario': inventario})

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas.html', {'ventas': ventas})

def detalles_venta(request):
    detalles_venta = Detalles_Venta.objects.all()
    return render(request, 'detalles_venta.html', {'detalles_venta': detalles_venta})

def lista_comisiones(request):
    comisiones = Comisiones.objects.all()
    return render(request, 'comisiones.html', {'comisiones': comisiones})

def lista_departamentos(request):
    departamentos = Departamentos.objects.all()
    return render(request, 'departamentos.html', {'departamentos': departamentos})

def lista_pagos(request):
    pagos = Pagos.objects.all()
    return render(request, 'pagos.html', {'pagos': pagos})

def lista_cotizaciones(request):
    cotizaciones = Cotizacion.objects.all()
    return render(request, 'cotizaciones.html', {'cotizaciones': cotizaciones})

def lista_detalles_cotizacion(request):
    detalles = Cotizacion_Detalle.objects.all()
    return render(request, 'cotizacion_detalle.html', {'detalles': detalles})

def lista_compras_carro(request):
    compras = Compra_Carro.objects.all()
    return render(request, 'compras_carro.html', {'compras': compras})

def lista_compras_repuesto(request):
    compras = Compra_Repuesto.objects.all()
    return render(request, 'compras_repuesto.html', {'compras': compras})

def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores.html', {'proveedores': proveedores})

def bitacora_alertas(request):
    alertas = Bitacora_Alertas.objects.all()
    return render(request, 'bitacora_alertas.html', {'alertas': alertas})

def historial_cambio(request):
    cambios = Historial_Cambio.objects.all()
    return render(request, 'historial_cambio.html', {'cambios': cambios})

def cambios_salarios(request):
    cambios = Cambios_Salarios.objects.all()
    return render(request, 'cambios_salarios.html', {'cambios': cambios})
