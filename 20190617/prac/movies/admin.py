from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_origin', 'vote_count', 'open_date', 'genre', 'score', 'poster_url', 'description')

admin.site.register(Movie, MovieAdmin)