
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from . forms import ProfesorForm


def curso(req, nombre, camada):
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()

    return HttpResponse(f""" 
      <p> Curso:{curso.nombre} Camada : {curso.camada} creado con exito!</p>
   """)


def listar_cursos(req):
    lista = Curso.objects.all()

    return render(req, "lista_curso.html", {"lista_curso": lista})


def inicio(req):
    return render(req, "inicio.html")


def cursos(req):
    return render(req, "cursos.html")


def profesores(req):
    return render(req, "profesores.html")


def estudiantes(req):
    return render(req, "estudiantes.html")


def entregables(req):
    return render(req, "entregables.html")


def listaProfesor(req):
    if req.method == 'POST':
        form = ProfesorForm(req.POST)
        if form.is_valid():
            form.save()

    else:
        form = ProfesorForm()
    return render(req, 'listaProfesores.html', {'form': form})
