from secrets import choice
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Employee
from .forms import RegisterEmployee

# Create your views here.

def relatorio_table(request):
    if request.method == 'POST':
        form = RegisterEmployee(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:Login')
    else:
        form = RegisterEmployee()
    return render(request, 'relatorio_pages/create.html', {'form':form})