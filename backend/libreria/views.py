from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm

# Create your views here.


def inicio(req):
    # return HttpResponse("<h1>Bienvenido Weizman</h1>")
    return render(req, 'paginas/inicio.html')


def nosotros(req):
    return render(req, 'paginas/nosotros.html')


def libros(req):
    libros = Libro.objects.all()
    print('get All libros', len(libros))
    return render(req, 'libros/index.html', {'libros': libros})


def crearLibro(req):
    formulario = LibroForm(req.POST or None)
    # print(formulario)
    return render(req, 'libros/crear.html', {'formulario', formulario})


def editarLibro(req):
    return render(req, 'libros/editar.html')
