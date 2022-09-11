# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import artirst, album, song, playlist


@admin.register(artirst)
class artirstAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(album)
class albumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year', 'artirst')
    list_filter = ('artirst',)
    search_fields = ('name',)


@admin.register(song)
class songAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'duration', 'year', 'album', 'artirst')
    list_filter = ('album', 'artirst')
    search_fields = ('name',)


@admin.register(playlist)
class playlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_filter = ('user',)
    raw_id_fields = ('playlist_songs',)
