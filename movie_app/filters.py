import django_filters
from .models import Movie, Director, Actor


class MovieFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(field_name='movie__title', label='Movie title', lookup_expr='icontains')
    director = django_filters.CharFilter(field_name='director__name', label='Director', lookup_expr='icontains')
    actor_name = django_filters.CharFilter(field_name='actors__name', label='Actor', lookup_expr='icontains')

    class Meta:
        model = Movie
        fields = ['actor_name', 'title', 'director']


class DirectorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Director
        fields = ['name']

class ActorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Actor
        fields = ['name']