from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.filter_carros, name='home'),
    path('login/', views.custom_login, name='login'),
    path('pruebarepuestos',views.filter_carros, name='pruebarepuestos'),
    # path('login/', views.login_view, name='login'),
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('carros/', views.lista_carros, name='lista_carros'),
    path('repuestos/', views.lista_repuestos, name='lista_repuestos'),
    path('inventario/', views.lista_inventario, name='lista_inventario'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('ventas/', views.lista_ventas, name='lista_ventas'),
    path('detalles-venta/', views.detalles_venta, name='detalles_venta'),
    path('comisiones/', views.lista_comisiones, name='lista_comisiones'),
    path('departamentos/', views.lista_departamentos, name='lista_departamentos'),
    path('pagos/', views.lista_pagos, name='lista_pagos'),
    path('cotizaciones/', views.lista_cotizaciones, name='lista_cotizaciones'),
    path('cotizacion_detalles/', views.lista_detalles_cotizacion, name='lista_detalles_cotizacion'),
    path('compras_carro/', views.lista_compras_carro, name='lista_compras_carro'),
    path('compras_repuesto/', views.lista_compras_repuesto, name='lista_compras_repuesto'),
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('bitacora_alertas/', views.bitacora_alertas, name='bitacora_alertas'),
    path('historial_cambio/', views.historial_cambio, name='historial_cambio'),
    path('cambios_salarios/', views.cambios_salarios, name='cambios_salarios'),
    path('vendedor-menu/', views.vendedor_menu_view, name='vendedor_menu'),
    path('menu/', views.menu_view, name='menu'),
    # path('inventario/', views.inventario_view, name='inventario'),
    # path('venta/', views.venta_view, name='venta'),
    # path('cotizacion/', views.cotizacion_view, name='cotizacion'),
    # path('admin/', views.administrador, name='admin'),
    # path('contador/', views.contador, name='contador'),
    # path('vendedor/', views.vendedor, name='vendedor'),
    # path('comprador/', views.comprador, name='comprador'),
    path('admin-menu/', views.admin_menu_view, name='admin_menu'),
    # path('pagos/', views.pagos_view, name='pagos'),
    path('cierres-mensuales/', views.cierres_mensuales_view, name='cierres_mensuales'),
    # path('empleados/', views.empleados_view, name='empleados'),
    path('control-usuario/', views.control_usuario_view, name='control_usuario'),
    # path('contador-menu/', views.contador_menu_view, name='contador_menu'),
    # path('gastos/', views.gastos_view, name='gastos'),
    # path('pagos/', views.pagos_view, name='pagos'),
    # path('comisiones/', views.comisiones_view, name='comisiones'),
    # path('ventas/', views.ventas_view, name='ventas'),
    # path('cierre-mensual/', views.cierre_mensual_view, name='cierre_mensual'),
    # path('comprador-menu/', views.comprador_menu_view, name='comprador_menu'),
    # path('carro/', views.carro_view, name='carro'),
    # path('repuesto/', views.repuesto_view, name='repuesto'),


]