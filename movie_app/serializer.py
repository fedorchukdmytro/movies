from rest_framework import serializers
from .models import Movie, Director, Actor

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class SimpleMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)

class ActorSerializer(serializers.ModelSerializer):
    movies = SimpleMovieSerializer(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = ('id', 'name', 'movies')

class SimpleActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name',)

class MovieSerializer(serializers.ModelSerializer):
    actors = SimpleActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
    
    

