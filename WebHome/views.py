
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from .models import Proveedor

#-----------------------------------------------------------------------------------------------------------------------------------------------

def home(request):
    return render(request, "WebHome/home.html")


# Ingresar ussuario / login user
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            userauth=form.cleaned_data.get('username')
            passwordauth=form.cleaned_data.get('password')
            
            user=authenticate(username=userauth, password=passwordauth)

            if user is not None:
                login(request, user)
                return render(request, 'WebHome/home.html', {'userlogin':userauth, 'messaje':f'Welcome {userauth} to Mikrotik Blog!!'})
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