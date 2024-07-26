from django.shortcuts import render, get_object_or_404
from animeflv import AnimeFLV

def home(request):
    query = request.GET.get('q', '')
    anime_list = []

    if query:
        try:
            with AnimeFLV() as api:
                anime_list = api.search(query)
        except Exception as e:
            print(f"Error searching for anime: {e}")

    return render(request, 'anime/home.html', {'anime_list': anime_list, 'query': query})

def anime_detail(request, anime_id):
    anime_info = None
    episodes = []

    try:
        with AnimeFLV() as api:
            anime_info = api.get_anime_info(anime_id)
            episodes = api.get_episodes(anime_id)
    except Exception as e:
        print(f"Error fetching anime info or episodes: {e}")

    return render(request, 'anime/detail.html', {'anime_info': anime_info, 'episodes': episodes})

def watch_episode(request, anime_id, episode_number):
    video_servers = []

    try:
        with AnimeFLV() as api:
            video_servers = api.get_video_servers(anime_id, episode_number)
    except Exception as e:
        print(f"Error fetching video servers: {e}")

    return render(request, 'anime/watch.html', {'video_servers': video_servers, 'anime_id': anime_id, 'episode_number': episode_number})
