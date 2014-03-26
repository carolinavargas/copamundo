from django.shortcuts import render
from django.views.generic import ListView
from models import Continente, Jugador


# Create your views here.

class ListarContinentes(ListView):
    model = Continente
    template_name = 'lista_continentes.html'


class ListarJugadores(ListView):
    model = Jugador
    template_name = 'lista_jugadores.html'
