from operator import index
from django.urls import path
from .views import *

#-----------------------------------------------------------------------------------------------------------------------------------------------

urlpatterns = [
    
    path('', home, name='home'),
    path('login', login_request, name='login'),

]