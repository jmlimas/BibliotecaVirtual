from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     
    url(r'^admin/', include(admin.site.urls)),

	url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root': settings.MEDIA_ROOT, } ),

    #inicio
    url(r'^',include('app.inicio.urls')),
    #autores
    url(r'^autor/',include('app.autores.urls')),

    #libros
    url(r'^libros/',include('app.libros.urls')),
)
