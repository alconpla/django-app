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
    awards = json_data['Awards']
    try: 
        rating = json_data['imdbRating']
        # rating = ratings[1]['Value']
    except:
        rating = 'No rating'

    context = {'title': title, 'rated': rated, 'released': released, 'runtime': runtime, 'genre': genre, 'director': director, 'actors': actors, 'plot': plot, 'poster': poster, 'rating': rating, 'awards': awards}
    return render(request, 'moviedetail.html', context)

# def custom_login(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')
    
#     user = authenticate(request, username=username, password=password)

#     if user is not None:
#         login(request, user)
        
#     return HttpResponseRedirect(reverse('home:home'))

# def custom_logout(request):
#     if request.user.is_authenticated:
#         logout(request)

#     return HttpResponseRedirect(reverse('home:home'))

# def custom_signup(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             form = SignupForm(request.POST)
            
#             if form.is_valid():
#                 new_user = form.save()
#                 display_name = form.cleaned_data.get('display_name')
#                 bio = form.cleaned_data.get('bio')
                
#                 new_user.profile = Profile()
#                 new_user.profile.display_name = display_name
#                 new_user.profile.bio = bio
#                 new_user.profile.save()

#                 username = form.cleaned_data.get('username')
#                 raw_password = form.cleaned_data.get('password1')
#                 user = authenticate(username=username, password=raw_password)
                
#                 login(request, user)
#                 return HttpResponseRedirect(reverse("home:home"))
#         else:
#             form = SignupForm()
        
#         replacements = {
#             'form': form
#         }

#         return render(request, 'users/create-account.html', replacements)
#     else:
#         return HttpResponseRedirect(reverse('home:home'))