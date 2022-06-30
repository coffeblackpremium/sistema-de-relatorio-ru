from secrets import choice
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterEmployee, TableEventForm
from django.contrib.auth.decorators import login_required
from .decorators import user_required
# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = RegisterEmployee(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/test')
    else:
        form = RegisterEmployee()
    return render(request, 'users/register.html', {'form':form})

def login_user(request):
    return render(request, 'users/login.html')


#Formulario de Registro de Evento do Usuario
@login_required(login_url='contas/login')
@user_required
def table_event(request):
    if request.method == 'POST':
        form = TableEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TableEventForm()
    return render(request, 'users/tableEvent/tableEventRegister.html', {'form':form})