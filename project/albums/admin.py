from django.contrib import admin
from .models import Albums, Musician

@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name')
    list_display = ('first_name', 'last_name', 'instrument')

@admin.register(Albums)
class AlbumsAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('name', )
    list_display = ('artist', 'name', 'date', 'stars')