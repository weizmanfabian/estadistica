from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def inicio(req):
    # return HttpResponse("<h1>Bienvenido Weizman</h1>")
    return render(req, 'paginas/inicio.html')


def nosotros(req):
    return render(req, 'paginas/nosotros.html')


def libros(req):
    return render(req, 'libros/index.html')


def crearLibro(req):
    return render(req, 'libros/crear.html')


def editarLibro(req):
    return render(req, 'libros/editar.html')
