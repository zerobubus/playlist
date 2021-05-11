from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager

User = get_user_model()


class Track(models.Model):
    title = models.CharField(verbose_name="трек", max_length=50)
    tags = TaggableManager()

    def __str__(self):
        return self.title


class Playlist(models.Model):
    name = models.CharField(verbose_name="плейлист", max_length=50)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="authors",
        verbose_name="автор"
    )
    track = models.ManyToManyField(Track)

    def __str__(self):
        return self.name
