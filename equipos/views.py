from django.shortcuts import render
from django.views.generic import ListView
<<<<<<< HEAD
from django.http import Http404
from models import Continente, Jugador, Equipo
=======
from models import Continente, Jugador
>>>>>>> ae4330770f2a2d791219d7dd45539ec1696aeaec


# Create your views here.

<<<<<<< HEAD

=======
>>>>>>> ae4330770f2a2d791219d7dd45539ec1696aeaec
class ListarContinentes(ListView):
    model = Continente
    template_name = 'lista_continentes.html'

<<<<<<< HEAD
class ListarEquipos(ListView):
    model = Equipo
    template_name = 'lista_equipos.html'

class ListarJugadores(ListView):
    model = Jugador
    template_name = 'listar_jugadores.html'



def detalleJugador(request, jugador_id):
    try:
        jugador = Jugador.objects.get(pk=jugador_id)
    except Jugador.DoesNotExist:
        raise Http404
    return render(request, 'player.html', {'jugador': jugador})
=======

class ListarJugadores(ListView):
    model = Jugador
    template_name = 'lista_jugadores.html'
>>>>>>> ae4330770f2a2d791219d7dd45539ec1696aeaec
