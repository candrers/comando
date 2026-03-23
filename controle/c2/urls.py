from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', logar_usuario, name="logar_usuario"),
    path('index', index, name="index"),
    path('logout', logout, name="logout"),
    path('chat', chat, name="chat"),
    path('map', map, name="map"),
    path('interest', interest, name="interest"),
]
