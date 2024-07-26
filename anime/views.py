

from django.shortcuts import render
from animeflv import AnimeFLV

def home(request):
    anime_list = []
    anime_info = {}
    video_servers = []
    
    with AnimeFLV() as api:
        search_results = api.search("Naruto")  # Buscar anime como ejemplo
        
        if search_results:
            anime_list = search_results
            first_anime_id = search_results[0]['id']
            
            try:
                anime_info = api.get_anime_info(first_anime_id)  # Obtener información del primer resultado de búsqueda
                video_servers = api.get_video_servers(first_anime_id)  # Obtener servidores de video del primer resultado
            except Exception as e:
                print(f"Error fetching anime info or video servers: {e}")
    
    return render(request, 'anime/home.html', {
        'anime_list': anime_list,
        'anime_info': anime_info,
        'video_servers': video_servers
    })
