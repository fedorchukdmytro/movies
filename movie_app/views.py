from django.shortcuts import render
from rest_framework import generics
from .models import Movie, Director, Actor
from .serializer import DirectorSerializer, ActorSerializer, MovieSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MovieFilter, DirectorFilter, ActorFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests


@api_view(['GET', 'POST'])
def add_movie(request, pk=None, *args, **kwargs):
    if request.method == 'GET':
        response = requests.get(f'http://www.omdbapi.com/?t={pk}&apikey=df9c5c5b')
        response = response.json()
        title = response.get("Title")
        # year = response.get("Year")
        rated = response.get("Released")
        released = response.get("Runtime")
        runtime = response.get("Genre")
        genre = response.get("Genre")
        # director = response.get("Director")
        writer = response.get("Writer")
        actor =response.get("Actors")
        plot = response.get("Plot")
        language = response.get("Language")
        country = response.get("Country")
        awards = response.get("Awards")          

        print(title,actor)
        if not Movie.objects.filter(title=title).exists():
            new_movie = Movie.objects.create(title=title,rated=rated,released=released,
                                             runtime=runtime,
                                             genre=genre,
                                             writer=writer, plot=plot, language=language, 
                                             country=country, awards=awards)
        # titanic = Movie.objects.create(name='Titanic')
        # laborday = Movie.objects.create(name='Labor Day')
            actors = actor.split(', ')
            for fullname in actors:
                if not Actor.objects.filter(name=fullname).exists():
                    actor = Actor.objects.create(name=fullname)
                    new_movie.actors.add(actor)
                else:
                    actor = Actor.objects.filter(name=fullname)
                    for act in actor:
                        new_movie.actors.add(act)
                        new_movie.save()

        return Response({"message": response})
    



class DirectorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class ActorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MovieFilter

class MovieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MovieFilter

class DirectorListAPIView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DirectorFilter

class ActorListAPIView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ActorFilter