from django.urls import path
from . import views

urlpatterns = [ 
    path("", views.index, name="index"), 
    path("new/", views.new_post, name="new_playlist"), 
    path("playlist/<int:playlist_id>/", views.playlist_view, name="playlist"), 
    path("playlist_confirm/<int:playlist_id>/", views.confirm_delete, name="playlist_confirm"), 
    path("playlist_delete/<int:playlist_id>/", views.playlist_delete, name="playlist_delete"), 
    path("playlist/<int:playlist_id>/edit/", views.post_edit, name="playlist_edit"), 
] 
