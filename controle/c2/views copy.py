from multiprocessing import Value
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import subprocess
import os
import glob
import shutil
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
def resources(request):
    return render(request, 'resources.html')

@login_required
def interest(request):
    
    if request.method == "POST":
        form = NAMEForm(request.POST)
        if form.is_valid():
            subs='value'
            texto= str(NAMEForm(request.POST))
            posicao = texto.find(subs)
            i = posicao + 6
            a =''
            for subs in texto:
                if texto[i] != '"':
                  a = a + texto[i]
                  i = i + 1
            print (a)
            source = '/tmp/'
            destination = '/home/carlos/comando/controle/c2/docs'
            allfiles = glob.glob(os.path.join(source, '*' + a + '*'), recursive=True)
            #allfiles = glob.glob(os.path.join(source, '*' + 'tank' + '*'), recursive=True)
            print("Files to move", allfiles)

            for file_path in allfiles:
                dst_path = os.path.join(destination, os.path.basename(file_path))
                shutil.move(file_path, dst_path)
                print(f"Moved {file_path} -> {dst_path}")

        return redirect(reverse('interest'))
    else:
        form = NAMEForm()
    
    return render(request, 'interest.html', {'form': form})