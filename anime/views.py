from django.shortcuts import render
from animeflv import AnimeFLV

def home(request):
    anime_list = []
    anime_info = None
    video_servers = []
    
    try:
        with AnimeFLV() as api:
            search_results = api.search("Naruto")  # Buscar "naruto" como ejemplo
            print(f"Search results: {search_results}")  # Imprimir resultados de la búsqueda

            if not search_results:
                print("No anime found.")
            else:
                anime_list = search_results
                first_anime = search_results[0]

                try:
                    anime_info = api.get_anime_info(first_anime.id)  
                    video_servers = api.get_video_servers(first_anime.id) 
                    print(f"Anime info: {anime_info}") 
                    print(f"Video servers: {video_servers}") 
                except Exception as e:
                    print(f"Error fetching anime info or video servers: {e}")
    except Exception as e:
        print(f"Error connecting to AnimeFLV API: {e}")
    
    return render(request, 'anime/home.html', {
        'anime_list': anime_list,
        'anime_info': anime_info,
        'video_servers': video_servers
    })
