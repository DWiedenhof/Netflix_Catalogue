from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .filters import MoviesFilter

# Create your views here.

def home(request):
    movies = Movies.objects.all()
    tableFilter = MoviesFilter(request.GET, queryset=movies)
    movies = tableFilter.qs

    context = {'movies': movies, 'tableFilter': tableFilter}
    return render(request, 'netcat/dashboard.html', context)

def title(request):
    titles = Titles.objects.all()
    return render(request, 'netcat/title.html', {'titles': titles})