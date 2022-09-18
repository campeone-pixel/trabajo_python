from django.shortcuts import render
from app_entrega1.models import *
from app_entrega1.forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, logout, authenticate

################----------------------------------################
def login_request(request):
  if request.method=='POST':
    form=AuthenticationForm(request,data=request.POST)
    if form.is_valid():
      usu=form.cleaned_data.get('username')
      clave=form.cleaned_data.get('password')
      usuario=authenticate(username=usu,password=clave)
      
      if usuario is not None:
        login(request,usuario)
        return render(request,'app_entrega1/index.html')
      else:
        return render(request,'app_entrega1/login_request.html')
    else:
      return render(request,'app_entrega1/login_request.html')
  else:
    form=AuthenticationForm()
    return render(request,"app_entrega1/login_request.html",{'form':form})

def register(request):
  if request.method =="POST":
    form = UserRegisterForm(request.POST)

    if form.is_valid():
      
      form.save()
      return render(request, "app_entrega1/index.html", {"mensaje":'Usuario creado'})

  else:
    form=UserRegisterForm()

  return render(request, "app_entrega1/register.html", {"form":form})

################---------------------------------

def index(request):
  return render(request, 'app_entrega1/index.html', )

def contacto(request):
  pass

def shopping(request):
  pass



