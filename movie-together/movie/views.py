from django.shortcuts import render

# Create your views here.

from movie.models import Movie
from movie.serializers import MovieSerializer
from rest_framework import generics

class MovieListCreate(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer