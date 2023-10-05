from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import HttpResponseRedirect, redirect, render, reverse

from .forms import UserRegisterForm
from .models import Employee

# Create your views here.


def index_view(request):
    return render(request, 'hr/index.html')

@login_required(login_url='/login/')
def search_view(request):
    idnumber = request.GET.get('idnumber', '')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    employees = Employee.objects.all()

    if idnumber:
        employees = employees.filter(nationalidnumber__startswith=idnumber)

    if start_date and end_date:
        employees = employees.filter(hiredate__range=[start_date, end_date])

    context = {
        'employees': employees,
        'idnumber': idnumber,
        'start_date': start_date,
        'end_date': end_date,
    }

    return render(request, 'hr/employees.html', context)

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Usuario registrado satisfactoriamente.')
            return HttpResponseRedirect(reverse('employees'))
        else:
            messages.error(request, 'Registro invalido. Algunos datos son incorrectos.')
    else:
        form = UserRegisterForm()

    context = {'register_form': form}
    return render(request, 'hr/register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(
                    request, f"Bienvenido! Iniciaste sesión como {username}.")
                return redirect('/employees/')
        else:
            messages.error(request, 'Usuario o contraseña incorrecta.')
    else:
        form = AuthenticationForm()

    context = {
        'login_form': form
    }
    return render(request, 'hr/login.html', context)

def logout_view(request):
    logout(request)
    messages.info(request, 'Se ha cerrado su sesión correctamente.')
    return redirect('/login/')