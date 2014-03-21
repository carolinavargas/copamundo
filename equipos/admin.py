
from django.contrib import admin
from models import Equipo, Continente, Jugador

# Register your models here.

class EquipoAdmin(admin.ModelAdmin):
    list_display=('nombre', 'continente', 'tecnico',)


class ContinenteAdmin(admin.ModelAdmin):
    list_display=('nombreContinente',)

class JugadorAdmin(admin.ModelAdmin):
    list_display=('nombreJugador','posicion','equipo','estatura','pieHabil','tarjetaRoja','tarjetaAmarilla','lesionado','titular','goles','foto',)

admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Continente, ContinenteAdmin)
admin.site.register(Jugador, JugadorAdmin)
