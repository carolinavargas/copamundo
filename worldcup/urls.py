from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import equipos.views
<<<<<<< HEAD
 
=======

>>>>>>> ae4330770f2a2d791219d7dd45539ec1696aeaec
admin.autodiscover()
 
urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
<<<<<<< HEAD
    url(r'^continentes/',equipos.views.ListarContinentes.as_view(), name='lista-continentes',),
    url(r'^jugadores/',equipos.views.ListarJugadores.as_view(), name='listar-jugadores',),
    url(r'^equipos/',equipos.views.ListarEquipos.as_view(), name='lista-equipos',),
    url(r'^player/(?P<jugador_id>\d+)/player.html$',
                'equipos.views.detalleJugador', name='detalle-jugador'),
=======
    url(r'^continentes/', equipos.views.ListarContinentes.as_view(), name='lista-continentes',),
    url(r'^jugadores/', equipos.views.ListarJugadores.as_view(), name='lista-jugadores',),
>>>>>>> ae4330770f2a2d791219d7dd45539ec1696aeaec

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
                {'document_root':settings.MEDIA_ROOT,}
       ),
)
<<<<<<< HEAD

 
=======
>>>>>>> ae4330770f2a2d791219d7dd45539ec1696aeaec
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
