from django.shortcuts import render, redirect
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/index.html', context)

def create(request):
    return render(request, 'movies/create.html')

def detail(request, pk):
    movies = Movie.objects.get(pk=pk)
    context = {'movies': movies}
    return render(request, 'movies/detail.html', context)

def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        movie.delete()
        return redirect('delete')
    else:
        return render(request, 'movies/detail.html')