from multiprocessing import Value
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import subprocess
from .forms import NAMEForm
from django.http import HttpResponseRedirect
from django.urls import reverse



# Create your views here.

def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})

@login_required
def index(request):
    
    return render(request, 'index.html')

@login_required
def logout(request):
    return render(request, 'logout.html')

@login_required
def chat(request):   

    subprocess.Popen('python3 /home/carlos/comando/controle/scripts/client.py', shell=True)
       
    return render(request,'chat.html',{})

@login_required
def map(request):
    return render(request, 'map.html')

@login_required
def interest(request):
    return render(request, 'interest.html')
