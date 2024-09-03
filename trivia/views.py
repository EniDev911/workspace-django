from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import Categoria, Pregunta
from .forms import UserForm, CrearCategoriaForm, CrearPreguntasForm, RespuestaForm
from django.contrib.auth.decorators import login_required
import random

def home_view(request: HttpRequest):
    return render(request, 'home.html')

def register_view(request: HttpRequest):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_url')
    else:
        form = UserForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def preguntas_view(request: HttpRequest):
    if request.user.is_superuser:
        preguntas = Pregunta.objects.all()
        return render(request, 'preguntas.html', {'preguntas': preguntas})

@login_required
def crear_pregunta_view(request: HttpRequest):
    if request.method == "POST" and request.user.is_superuser:
        form = CrearPreguntasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('preguntas_url')
    else:
        form = CrearPreguntasForm()
    return render(request, 'crear_pregunta.html', {'form': form})

def eliminar_pregunta_view(request: HttpRequest, id):
    pregunta = get_object_or_404(Pregunta, pk=id)
    if request.method == "POST":
        pregunta.delete()
        return redirect('preguntas_url')

@login_required
def juego_view(request: HttpRequest):
    query = "SELECT *"
    query += " FROM trivia_pregunta AS p"
    query += " INNER JOIN trivia_categoria AS c"
    query += " ON p.categoria_id_id = c.id"
    query += " ORDER BY random() limit 4"
    preguntas = Pregunta.objects.raw(query)
    if not preguntas:
        return render(request, 'juego.html', {'mensaje': 'No hay preguntas disponibles'})

    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if form.is_valid():
            # respuesta_usuario = form.cleaned_data['respuesta']
            # respuesta_correcta = pregunta.respuestas.filter(resp_correcta=True).first()
            # if respuesta_usuario == respuesta_correcta.texto:
                # return render(request, 'trivia/resultados.html', {'resultado': 'Correcto'})
            # else:
                # return render(request, 'trivia/resultados.html', {'resultado': 'Incorrecto'})
            print(form.cleaned_data)
    else:
        form = RespuestaForm()

    return render(request, 'juego.html', {
        'preguntas': preguntas,
        'form': form
    })

@login_required
def crear_categoria(request:HttpRequest):
    if request.method == "POST" and request.user.is_superuser:
        form = CrearCategoriaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            categoria = Categoria(nombre=nombre)
            categoria.save()
            return redirect('crear_pregunta_url')
    else:
        form = CrearCategoriaForm()
    return render(request, 'crear_categoria.html', {'form': form})