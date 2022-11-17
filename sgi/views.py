import datetime

from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from .models import *


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    prioriy = forms.IntegerField(label="Priority", min_value=1, max_value=10)


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('tasks:login'))
    

    if "tasks" not in request.session:
        request.session["tasks"] = []
    now = datetime.datetime.now()
    return render (request, "sgi/index.html", {
        "newyear": now.month ==1 and now.day ==1,
        "tasks": request.session["tasks"],
        "funcionarios": Funcionario.objects.all(),
    })

def login_view (request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('tasks:add'))
        else:
            return render(request, "sgi/home.html", {
                "message": "Nao Cadastrado"
            })
    return render(request, "sgi/home.html")

def logout_view(request):
    logout(request)
    return render(request, "sgi/home.html", {
        "message": "Logged Out"
    })


def funcionario(request, funcionario_id):
    funcionario = Funcionario.objects.get(pk=funcionario_id)
    turnos = funcionario.turnoatual.all()
    return render(request, "sgi/funcionario.html", {
        "funcionario": funcionario,
        "turnos": turnos,
        "armario": Armario.objects.all(),
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "sgi/add.html", {
                "form": form
            })
    return render(request, "sgi/add.html", {
        "form": NewTaskForm(),
    })

def brian(request):
    return HttpResponse("Hello, Brian")

def greet(request, name):
    return render (request, "sgi/greet.html", {"name": name.capitalize()})

def cadastro(request, funcionario_id):
    if request == "POST":
       funcionario = Funcionario.objects.get(pk=funcionario_id)
       armario = Armario.objects.get(pk=request.POST["armario"])
       armario.funcionario.add(funcionario)
       return HttpResponseRedirect("funcionario", args="funcionario.id")

def sobre(request):
    return render(request, "sgi/sobre.html")

def start(request):
    empregados = Employee.objects.all()
    return render(request, "sgi/start.html", {"empregados": empregados})

def salvar(request):
    name = request.POST.get('nome')
    register = request.POST.get('registro')
    area = request.POST.get('area')
    patrimonio = request.POST.get('patrimonio')
    posicao = request.POST.get('posicao')
    localizacao = request.POST.get('localizacao')
    Funcionario.objects.create(nome=name, registro=register, posto=area)
    Armario.objects.create(patrimonio=patrimonio, funcionario=Funcionario(nome=name,registro=register, posto=area), posicao=posicao, localizacao=localizacao)
    empregados = Employee.objects.all()
    armarios = Armario.objects.all()
    return render(request, "sgi/start.html", {
        "empregados": empregados
        })

def editar(request, id):
    empregado = Employee.objects.get(id=id)
    return render(request, "sgi/update.html", {"empregado": empregado})

def update(request, id):
    name = request.POST.get('nome')
    register = request.POST.get('registro')
    area = request.POST.get('area')
    empregado = Employee.objects.get(id=id)
    empregado.name = name
    empregado.register = register
    empregado.area = area
    empregado.save()
    return redirect("tasks:start")

def delete(request, id):
    empregado = Employee.objects.get(id=id)
    empregado.delete()
    return redirect("tasks:start")

def cadastrar(request):
    return render(request, "sgi/cadastro_view.html")