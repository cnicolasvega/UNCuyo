from operator import index
from django.urls import path
from .views import *
from django.conf.urls.static import static

#-----------------------------------------------------------------------------------------------------------------------------------------------

urlpatterns = [
    
    path('', home, name='home'),
    path('sitios/', sitios, name='sitios'),
    path('buscar/', buscar, name='buscar'),
    path('login/', login_request, name='login'),

    path('macvendor/', macvendor, name='macvendor'),
    path('proveedores/', proveedores, name='proveedores'),
    path('listareclamos/', listareclamos, name='listareclamos'),
    path('reclamos/', ReclamoCreate.as_view(template_name="WebHome/reclamos.html"), name='reclamos'),
]