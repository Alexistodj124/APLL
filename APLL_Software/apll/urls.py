from django.urls import path
from . import views
urlpatterns = [
    path('', views.filter_carros, name='home'),
    path('login', views.login, name='login'),
    path('pruebarepuestos',views.filter_carros, name='pruebarepuestos'),

]