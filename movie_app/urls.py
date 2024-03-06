from django.urls import path
from .views import *

urlpatterns = [
    path('directors/', DirectorListCreateAPIView.as_view(), name='director-list-create'),
    path('directors/<int:pk>/', DirectorRetrieveUpdateDestroyAPIView.as_view(), name='director-detail'),

    path('actors/', ActorListCreateAPIView.as_view(), name='actor-list-create'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyAPIView.as_view(), name='actor-detail'),

    path('movies/', MovieListCreateAPIView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-detail'),

  
    path('movies1/<str:pk>/', add_movie, name='movie-list'),
    
]
