

import requests
import argparse
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Proveedor, Reclamos, Sitios
from django.views.generic.detail import DetailView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView


#-----------------------------------------------------------------------------------------------------------------------------------------------

def home(request):
    return render(request, "WebHome/home.html")


# Ingresar usuario / login user
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            userauth=form.cleaned_data.get('username')
            passwordauth=form.cleaned_data.get('password')
            
            user=authenticate(username=userauth, password=passwordauth)

            if user is not None:
                login(request, user)
                return render(request, 'WebHome/home.html', {'userlogin':userauth})
            else:
                return render(request, 'WebHome/login.html', {'form':form, 'messaje':'User incorrect'})
        else:
            return render(request, 'WebHome/login.html', {'form':form, 'messaje':'Invalid credentials, please check'})
    
    else:
        form=AuthenticationForm()
        return render(request, 'WebHome/login.html', {'form':form})


def proveedores(request):
    proveedor = Proveedor.objects.all().order_by('proveedor')
    context = {'proveedor':proveedor}

    return render(request, "WebHome/proveedores.html", context)

def sitios(request):
    sitio = Sitios.objects.all().order_by('sitio')
    context = {'sitio':sitio}

    return render(request, "WebHome/sitios.html", context)

def macvendor(request):
    return render(request, "WebHome/macvendor.html")

def listareclamos(request):
    return render(request, "WebHome/listareclamos.html")

def search_sitios(request):
    if request.GET["sitio"]:
        title = request.GET["title"]
        post = Sitios.objects.filter(title__icontains=title)
        return render(request, "WebHome/buscarsitio.html", {"post":post})
    else:
        response="Ingrese el nombre de un sitios"
    return render(request, "WebHome/buscarsitio.html", {"response":response})

#-----------------------------------------------------------------------------------------------------------------------------------------------

def get_arguments(): 
    
    parser = argparse.ArgumentParser() 
      
    parser.add_argument("-m", "--macaddress", 
                        dest="mac_address", 
                        help="MAC Address of the device. "
                        ) 
    options = parser.parse_args() 
      
    if options.mac_address: 
        return options.mac_address 
    else: 
        parser.error("[!] Invalid Syntax. "
                     "Use --help for more details.") 
  
def get_mac_details(mac_address): 

    url = "https://api.macvendors.com/"
      
    response = requests.get(url+mac_address) 
    if response.status_code != 200: 
        raise Exception("[!] Invalid MAC Address!") 
    return response.content.decode() 
  
if __name__ == "__main__": 
    mac_address = get_arguments() 
    print("[+] Checking Details...") 
      
    try: 
        vendor_name = get_mac_details(mac_address) 
        print("[+] Device vendor is "+vendor_name) 
    except: 
        print("[!] An error occured. Check "
              "your Internet connection.") 

def reclamos(request):
    return render(request, "WebHome/reclamos.html")


class ReclamoCreate(LoginRequiredMixin, CreateView):
    model = Reclamos
    template_name = 'WebHome/reclamos.html'
    success_url = reverse_lazy('listareclamos')
    fields = ['sitio',  'proveedor', 'contact', 'num', 'coment']
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            person=self.request.user
        )

def buscar(request):
    return render(request, "WebHome/buscar.html")