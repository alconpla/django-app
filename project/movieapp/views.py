from django.shortcuts import render
import requests
import json

class Pelicula:
    title = ''
    year = 0
    rated = ''
    poster = ''


# Create your views here.

def index(request):
    title = request.GET.get('search')
    if title != None:
        peliculas = getMovies(title, True)
        count = len(peliculas)

        context = {'peliculas': peliculas, 'count': count}
        return render(request, 'search.html', context)
    else:
        peliculas = getMovies('avengers')
        peliculas2 = getMovies('lord of the rings')
        peliculas3 = getMovies('john wick')

        context = {'peliculas': peliculas, 'peliculas2': peliculas2, 'peliculas3': peliculas3}
        return render(request, 'index.html', context)


def getMovies(title, search = False):
    response = requests.get("http://www.omdbapi.com/?s=" + title + "&type=movie&apikey=77074898")
    json_data = json.loads(response.text)
    aux = json_data['Search']
    iteration = len(aux)

    if not search:
        iteration = 3
        
    peliculas = []
    for p in range(iteration):
        aux_p = aux[p]
        pelicula = Pelicula()
        pelicula.title = aux_p['Title']
        pelicula.year = aux_p['Year']
        pelicula.poster = aux_p['Poster']

        peliculas.append(pelicula)
    
    return peliculas

def movie_detail(request, title):
    response = requests.get("http://www.omdbapi.com/?t=" + title + "&type=movie&apikey=77074898")
    json_data = json.loads(response.text)
    title = json_data['Title']
    rated = json_data['Rated']
    released = json_data['Released']
    runtime = json_data['Runtime']
    genre = json_data['Genre']
    director = json_data['Director']
    actors = json_data['Actors']
    plot = json_data['Plot']
    poster = json_data['Poster']
    # ratings

    context = {'title': title, 'rated': rated, 'released': released, 'runtime': runtime, 'genre': genre, 'director': director, 'actors': actors, 'plot': plot, 'poster': poster, }
    return render(request, 'moviedetail.html', context)