from django.contrib import admin
from .models import Board

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'image', 'updated_at',)

admin.site.register(Board, BoardAdmin)