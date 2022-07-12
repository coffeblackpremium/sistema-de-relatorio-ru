from secrets import choice
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login

from relatorios.models import TableActionModel, TableEventModel, User
from .forms import RegisterEmployee, TableActionForm, TableEventForm
from django.contrib.auth.decorators import login_required
from .decorators import user_required
from django.core.paginator import Paginator
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
        form_table_event = TableEventForm(request.POST)
        if form_table_event.is_valid():
            profile = form_table_event.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('/users/tabelas')
    else:
        form_table_event = TableEventForm()
    return render(request, 'tables/tableEvent/tableEventRegister.html', {'form_table_event':form_table_event})

@login_required(login_url='contas/login')
@user_required
def table_action(request):
    if request.method == 'POST':
        form_table_action = TableActionForm(request.POST)
        if form_table_action.is_valid():
            profile = form_table_action.save(commit=False)
            profile.user = request.user
            profile.save()
            form_table_action.save()
            return redirect('/users/tabelas')
    else:
        form_table_action = TableActionForm()
    return render(request, 'tables/tableAction/tableActionRegister.html', {'form_table_action':form_table_action})

@login_required(login_url='contas/login')
@user_required
def tables(request):
    tables_actions = TableActionModel.objects.filter(user=request.user).values().order_by('-id')
    tables_events = TableEventModel.objects.filter(user=request.user).values().order_by('-id')

    paginator_table_actions = Paginator(tables_actions, 5)
    paginator_table_events = Paginator(tables_events, 5)
    page_number_table_action = request.GET.get('page_action')
    page_number_table_event = request.GET.get('page_event')
    table_action_page_object = paginator_table_actions.get_page(page_number_table_action)
    table_event_page_object = paginator_table_events.get_page(page_number_table_event)

    return render(request, 'tables/viewAllTable.html',
    {
    'table_action_page_object':table_action_page_object,
    'table_event_page_object':table_event_page_object,})




@login_required(login_url='contas/login')
@user_required
def description_table(request, id):
    tables_actions = TableActionModel.objects.filter(user=request.user).values().order_by('-id')
    tables_events = TableEventModel.objects.filter(user=request.user).values().order_by('-id')
    id_description = get_object_or_404(tables_actions, id=id)

    paginator_table_actions = Paginator(tables_actions, 5)
    paginator_table_events = Paginator(tables_events, 5)
    page_number_table_action = request.GET.get('page_action')
    page_number_table_event = request.GET.get('page_event')
    table_action_page_object = paginator_table_actions.get_page(page_number_table_action)
    table_event_page_object = paginator_table_events.get_page(page_number_table_event)
    
    return render(request, 'tables/tableAction/tableActionGetDescription.html', 
    {'id_description':id_description,
    'table_action_page_object':table_action_page_object,
    'table_event_page_object':table_event_page_object})


@login_required(login_url='contas/login')
@user_required
def deleteTableAction(request, id):
    object_table_action = get_object_or_404(TableActionModel, id=id)

    if request.method == "POST":
        object_table_action.delete()
        return redirect("/users/tabelas")
    return render(request, "delete_view.html")

@login_required(login_url='contas/login')
@user_required
def deleteTableEvent(request, id):
    object_table_event = get_object_or_404(TableEventModel, id=id)
    if request.method == "POST":
        object_table_event.delete()
        return redirect('/users/tabelas')
    return render(request, "delete_view.html")


@login_required(login_url='contas/login')
@user_required
def table_action_update(request, id):
    context = {}

    get_object_model = get_object_or_404(TableActionModel, id=id)
    form = TableActionForm(request.POST or None, instance=get_object_model)

    if form.is_valid():
        form.save()
        return redirect('/users/tabelas')
    context['form_table_action'] = form
    return render(request, "tables/tableAction/tableActionUpdate.html", context=context)

@login_required(login_url='contas/login')
@user_required
def table_event_update(request, id):
    context = {}
    get_object_model = get_object_or_404(TableEventModel, id=id)
    form = TableEventForm(request.POST or None, instance=get_object_model)

    if form.is_valid():
        form.save()
        return redirect('/users/tabelas')
    context = {'form_table_event':form}
    return render(request, 'tables/tableEvent/tableEventUpdate.html', context=context)