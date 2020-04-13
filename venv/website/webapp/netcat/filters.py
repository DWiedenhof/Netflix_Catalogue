import django_filters

from .models import *

class MoviesFilter(django_filters.FilterSet):
    class Meta:
        model = Movies
        fields = '__all__'
