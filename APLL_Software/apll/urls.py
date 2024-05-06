from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.filter_carros, name='home'),
    path('login/', views.custom_login, name='login'),
    path('pruebarepuestos',views.filter_carros, name='pruebarepuestos'),

]