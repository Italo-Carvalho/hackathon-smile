from django.urls import include, path

from .views import *

urlpatterns = [
    path('', ViagemView, name='index'),
    path('ajax/load-locais/', load_locais, name='ajax_load_locais'),
    path('viajem/<int:pk>', ViagemEX, name='viagemex'),
    path('resultado/<int:pk>', Resultado, name='resultado'),
]
