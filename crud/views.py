from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import requests
from rest_framework.parsers import JSONParser

from crud.models import Movie, Ratings, Comments
from crud.serializers import MovieSerializer, RatingSerializer, CommentSerializer


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


def movies_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        json_list = []
        for movie in movies:
            ratings = Ratings.objects.filter(movie_id=movie.id)
            if ratings is not None:
                rating_sanitazer = RatingSerializer(ratings, many=True)
                serializer = MovieSerializer(movie)
                json_list.append({"movie": serializer.data, "ratings": rating_sanitazer.data})
        return JsonResponse(json_list, safe=False)


@csrf_exempt
def add_movie(request, title):
    if request.method == 'POST':
        data = requests.get('http://www.omdbapi.com/?apikey=b911964a&t=' + title)
        movie = Movie.objects.create(title=data.json()['Title'], year=data.json()['Year'], rated=data.json()['Rated'],
                                     released=data.json()['Released'], runtime=data.json()['Runtime'],
                                     genre=data.json()['Genre'], director=data.json()['Director'],
                                     writer=data.json()['Writer'], actors=data.json()['Actors'],
                                     plot=data.json()['Plot'], language=data.json()['Language'],
                                     country=data.json()['Country'], awards=data.json()['Awards'],
                                     poster=data.json()['Poster'], metascore=data.json()['Metascore'],
                                     imdb_rating=data.json()['imdbRating'], imdb_votes=data.json()['imdbVotes'],
                                     imdb_id=data.json()['imdbID'], type=data.json()['Type'], dvd=data.json()['DVD'],
                                     box_office=data.json()['BoxOffice'], production=data.json()['Production'],
                                     website=data.json()['Website'], response=bool(data.json()['Response']))
        movie.save()
        for element in data.json()['Ratings']:
            rating = Ratings.objects.create(source=element['Source'], value=element['Value'],
                                            movie_id=Movie.objects.latest('id'))
            rating.save()
    return HttpResponse("Dodano!")


def get_comments(request):
    if request.method == 'GET':
        comments = Comments.objects.all()
        if comments is not None:
            comment_serializer = CommentSerializer(comments, many=True)
            return JsonResponse(comment_serializer.data, safe=False)


def get_comments_by_id(request, id):
    if request.method == 'GET':
        comments = Comments.objects.filter(movie_id=id)
        if comments is not None:
            comment_serializer = CommentSerializer(comments, many=True)
            return JsonResponse(comment_serializer.data, safe=False)


@csrf_exempt
def add_comment(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
