from datetime import datetime
from django.http import HttpResponse
from .models import Carro
from django.shortcuts import redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
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
from .forms import EmpleadoForm
from .forms import UserForm

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
            # Check user's group membership
            if user.groups.filter(name='admin').exists():
                # Redirect admin users to a certain URL
                return redirect('admin_menu')
            elif user.groups.filter(name='ventas').exists():
                # Redirect ventas users to a different URL
                return redirect('vendedor_menu')
            else:
                messages.add_message(request, messages.ERROR, 'Usuario no pertenece a ningun GRUPO.')
        else:
            # Return an error message if authentication fails
            messages.error(request, 'Usuario o Contraseña Invalidos.')
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

    


@login_required
def menu_view(request):
    return render(request, 'menu.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def vendedor_menu_view(request):
    if request.user.groups.filter(name__in =['admin','ventas']).exists():
        return render(request, 'vendedor_menu.html')
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')

@login_required
def admin_menu_view(request):
    if request.user.groups.filter(name='admin').exists():
        return render(request, 'admin_menu.html')
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')

@login_required
def contador_menu_view(request):
    if request.user.groups.filter(name__in =['admin','contador']).exists():
        return render(request, 'contador_menu.html')
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')

def comprador_menu_view(request):
    return render(request, 'comprador_menu.html')

@login_required
def cierres_mensuales_view(request):
    if request.user.groups.filter(name='admin').exists():
        # Cambiar a URL CORRECTO
        return render(request, 'vendedor_menu.html')
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')

@login_required
def control_usuario_view(request):
    if request.user.groups.filter(name='admin').exists():
        # Cambiar a URL CORRECTO
        return redirect('/admin')
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')

@login_required
def lista_empleados(request):
    # new_employee = Empleados(EmpleadoDPI= 1234 ,Nombres='Alex', Apellidos='Gonzalez', Sueldo=4250.00)
    # new_employee.save()
    
    if request.user.groups.filter(name='admin').exists():
        empleados = Empleados.objects.all()
        return render(request, 'empleado.html', {'empleados': empleados})
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')

@login_required
def lista_carros(request):
    if request.user.groups.filter(name__in =['admin','ventas']).exists():
        carros = Carro.objects.all()
        return render(request, 'carros.html', {'carros': carros})
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')

@login_required
def lista_repuestos(request):
    if request.user.groups.filter(name__in =['admin','ventas']).exists():
        repuestos = Repuestos.objects.all()
        return render(request, 'repuestos.html', {'repuestos': repuestos})
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')

@login_required
def lista_inventario(request):
    if request.user.groups.filter(name__in =['admin','ventas']).exists():
        inventario = Inventario.objects.all()
        return render(request, 'inventario.html', {'inventario': inventario})
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')

@login_required
def lista_usuarios(request):
    if request.user.groups.filter(name='admin').exists():
        usuarios = Usuario.objects.all()
        return render(request, 'usuarios.html', {'usuarios': usuarios})
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')

@login_required
def lista_clientes(request):
    if request.user.groups.filter(name='admin').exists():
        clientes = Cliente.objects.all()
        return render(request, 'clientes.html', {'clientes': clientes})
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')

@login_required
def lista_ventas(request):
    if request.user.groups.filter(name__in =['admin','ventas']).exists():
        ventas = Venta.objects.all()
        return render(request, 'ventas.html', {'ventas': ventas})
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')

@login_required
def detalles_venta(request):
    if request.user.groups.filter(name='admin').exists():
        detalles_venta = Detalles_Venta.objects.all()
        return render(request, 'detalles_venta.html', {'detalles_venta': detalles_venta})
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')

@login_required
def lista_comisiones(request):
    if request.user.groups.filter(name='admin').exists():
        comisiones = Comisiones.objects.all()
        return render(request, 'comisiones.html', {'comisiones': comisiones})
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')

@login_required
def lista_departamentos(request):
    if request.user.groups.filter(name='admin').exists():
        departamentos = Departamentos.objects.all()
        return render(request, 'departamentos.html', {'departamentos': departamentos})
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')

@login_required
def lista_pagos(request, anio=None, mes=None):
    # venta = Venta.objects.create(
    #     Nombre_Cliente='Silvino',
    #     NIT = 112341234,
    #     Total = 1500.00,
    #     empleado = Empleados.objects.get(EmpleadoDPI=1234),
    # )
    # pago = Pagos.objects.create(
    #     MetodoPago='Tarjeta',
    #     Monto = 500.00,
    #     venta=Venta.objects.get(Numero_Orden=1)
    # )

    if request.user.groups.filter(name='admin').exists():
        pagos = Pagos.objects.all()
        pagos_filtrados = []
        for pago in pagos:
            fecha = str(pago.venta.Fecha)
            fecha_dt = datetime.fromisoformat(fecha)
            mes1 = str(fecha_dt.month)
            anio1 = str(fecha_dt.year)
            if anio1 == anio:
                if mes1 == mes:
                    pagos_filtrados.append(pago)
        print(pagos_filtrados)
        return render(request, 'pagos.html', {'pagos': pagos_filtrados})
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')
    
@login_required
def filtro_pagos(request):
    if request.user.groups.filter(name='admin').exists():
        if 'month' in request.GET:
            mes_anio = request.GET['month']
            anio1, mes1 = map(int, mes_anio.split('-'))
            return redirect('lista_pagos', anio=anio1, mes=mes1)
        return render(request, 'filtro_pagos.html')
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')

@login_required
def lista_cotizaciones(request):
    if request.user.groups.filter(name__in =['admin','ventas']).exists():
        cotizaciones = Cotizacion.objects.all()
        return render(request, 'cotizaciones.html', {'cotizaciones': cotizaciones})
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')

@login_required
def lista_detalles_cotizacion(request):
    if request.user.groups.filter(name='admin').exists():
        detalles = Cotizacion_Detalle.objects.all()
        return render(request, 'cotizacion_detalle.html', {'detalles': detalles})
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')

@login_required
def lista_compras_carro(request):
    if request.user.groups.filter(name='admin').exists():
        compras = Compra_Carro.objects.all()
        return render(request, 'compras_carro.html', {'compras': compras})
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')
        
@login_required
def lista_compras_repuesto(request):
    if request.user.groups.filter(name='admin').exists():
        compras = Compra_Repuesto.objects.all()
        return render(request, 'compras_repuesto.html', {'compras': compras})
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')

@login_required
def lista_proveedores(request):
    if request.user.groups.filter(name='admin').exists():
        proveedores = Proveedor.objects.all()
        return render(request, 'proveedores.html', {'proveedores': proveedores})
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')

@login_required
def bitacora_alertas(request):
    if request.user.groups.filter(name='admin').exists():
        alertas = Bitacora_Alertas.objects.all()
        return render(request, 'bitacora_alertas.html', {'alertas': alertas})
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')

@login_required
def historial_cambio(request):
    if request.user.groups.filter(name='admin').exists():
        cambios = Historial_Cambio.objects.all()
        return render(request, 'historial_cambio.html', {'cambios': cambios})
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')

@login_required
def cambios_salarios(request):
    if request.user.groups.filter(name='admin').exists():
        cambios = Cambios_Salarios.objects.all()
        return render(request, 'cambios_salarios.html', {'cambios': cambios})
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')
    
@login_required
def edit_empleado(request, empleadoDPI):
    if request.user.groups.filter(name='admin').exists():
        empleado = Empleados.objects.get(EmpleadoDPI=empleadoDPI)
        # Realiza las operaciones necesarias con el empleado_id, como buscar el empleado en la base de datos y mostrar un formulario de edición.
        print(empleado)
        return render(request, 'editar_empleado.html', {'empleado': [empleado]})
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')
    

@login_required
def empleadoCUD(request, empleadoDPI):
    if request.user.groups.filter(name='admin').exists():
        instance = get_object_or_404(Empleados, pk=empleadoDPI)
        if request.method == 'POST':
            form = EmpleadoForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('my_model_list')
        else:
            form = EmpleadoForm(instance=instance)
        return render(request, 'my_model_form.html', {'form': form})
    else:
        # El usuario no pertenece al grupo, redirigir o mostrar un mensaje de error
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('login')
    
def EditUser(request,id=None):
    one_rec=Empleados.objects.get(pk=id)
    form=UserForm(request.POST or None,request.FILES or None, instance=one_rec)
    if form.is_valid():
        form.save()
        return redirect('/empleados')
    mydict= {'form':form}
    return render(request,'editar_empleado.html',context=mydict)

def DeleteUser(request,eid=None):
    one_rec = Empleados.objects.get(pk=eid)
    if  request.method=="POST":
         one_rec.delete()
         return redirect('/empleados')
    return render(request,'Delete.html')