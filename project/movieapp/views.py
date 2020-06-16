from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import requests
import json
from .models import Pelicula

# class Pelicula:
#     title = ''
#     year = 0
#     rated = ''
#     poster = ''


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
    if request.method == 'POST':
        return mylist(request)
    else:
        user_not_logged = True
        movie_already_added = False
        if request.user.is_authenticated:
            user_not_logged = False
            my_movie = Pelicula.objects.filter(title=title, user=request.user).first()

            if not my_movie == None:
                movie_already_added = True

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
        awards = json_data['Awards']
        try: 
            ratings = json_data['Ratings']
            imdb = json_data['imdbRating']
            metascore = json_data['Metascore']
            rtomatoes = ratings[1]['Value']
        except:
            imdb = 'N/A'
            metascore = 'N/A'
            rtomatoes = 'N/A'

        context = {'title': title, 'rated': rated, 'released': released, 'runtime': runtime, 'genre': genre, 'director': director, 'actors': actors, 'plot': plot, 'poster': poster, 'imdb': imdb, 'metascore': metascore, 'rtomatoes': rtomatoes, 'awards': awards, 'user_not_logged': user_not_logged, 'movie_already_added': movie_already_added }
        return render(request, 'moviedetail.html', context)

def mylist(request):
    if request.user.is_authenticated:
        movie_title = request.POST.get('movie')
        if movie_title != None:
            response = requests.get("http://www.omdbapi.com/?t=" + movie_title + "&type=movie&apikey=77074898")
            pelicula = Pelicula()
            json_data = json.loads(response.text)
            pelicula.title = json_data['Title']
            pelicula.poster = json_data['Poster']
            pelicula.rated = json_data['Rated']
            pelicula.year = json_data['Year']
            pelicula.user = request.user
            pelicula.save()

    return HttpResponseRedirect(request.path_info)

def showlist(request):
    if request.user.is_authenticated:
        my_movies = Pelicula.objects.all().filter(user=request.user)
        count = len(my_movies)

        context = {'my_movies': my_movies, 'count':count}
        return render(request, 'showlist.html', context)

def delete_from_list(request, title):
    if request.user.is_authenticated:
        delete = Pelicula.objects.get(title=title, user=request.user).delete()
        return redirect('showlist')