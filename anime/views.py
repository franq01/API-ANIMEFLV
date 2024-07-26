# anime/views.py

from django.shortcuts import render
from animeflv import AnimeFLV

def home(request):
    with AnimeFLV() as api:
        anime_list = api.get_anime_list()  # Obtiene  la lista de animes
    return render(request, 'anime/home.html', {'anime_list': anime_list})
