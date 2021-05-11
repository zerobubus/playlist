from django.contrib import admin

from .models import Track, Playlist

class TrackAdmin(admin.ModelAdmin):
    
    list_display = ("pk", "title") 


class PlaylistAdmin(admin.ModelAdmin):
    
    list_display = ("id", "name", "user")    



admin.site.register(Track, TrackAdmin)
admin.site.register(Playlist, PlaylistAdmin)
