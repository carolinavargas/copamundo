from django.db import models

# Create your models here.

POSICIONES = (
     ('seleccione','Seleccione'),
     ('arquero','Arquero'),
     ('defensa','Defensa'),
     ('volante','Volante'),
     ('delantero','Delantero'),

)

PIEHABIL = (
     ('seleccione','Seleccione'),
     ('diestro','Diestro'),
     ('zurdo','Zurdo'),

)


class Continente(models.Model):
    nombreContinente = models.CharField(max_length=50)
    def __unicode__(self):
        return  self.nombreContinente

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    continente = models.ForeignKey(Continente)
    tecnico = models.CharField(max_length=60)
    def __unicode__(self):
        return self.nombre


class Jugador(models.Model):
    nombreJugador = models.CharField(max_length=60)
    posicion = models.CharField(choices=POSICIONES, default='seleccione', max_length=10)
    equipo = models.CharField(max_length=50)
    estatura = models.FloatField()
    pieHabil = models.CharField(choices=PIEHABIL, default='seleccione', max_length=10)
    tarjetaRoja = models.IntegerField (max_length=10)
    tarjetaAmarilla = models.IntegerField(max_length=50)
    lesionado = models.BooleanField()
    titular = models.BooleanField()
    goles = models.IntegerField()
    foto = models.ImageField(upload_to='images', verbose_name='Foto', null=True,)
    def __unicode__(self):
        return self.nombreJugador

