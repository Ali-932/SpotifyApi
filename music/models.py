from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver
import uuid
from smart_selects.db_fields import ChainedForeignKey

User = get_user_model()


# Create your models here.
class artirst(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class album(models.Model):
    name = models.CharField(max_length=25)
    year = models.CharField(max_length=4)
    artirst = models.ForeignKey(artirst, on_delete=models.SET_NULL, null=True, blank=True,related_name='albums')

    def __str__(self):
        return self.name


class song(models.Model):
    name = models.CharField(max_length=25)
    duration = models.CharField(max_length=6, null=True, blank=True)
    year = models.DecimalField(max_digits=4, decimal_places=0)
    album = models.ForeignKey(album, on_delete=models.SET_NULL, null=True, blank=True,related_name='song_album')
    artirst = models.ForeignKey(artirst, on_delete=models.SET_NULL, null=True, blank=True,related_name='artierst')

    def __str__(self):
        return self.name


class playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist_songs = models.ManyToManyField(song)

@receiver(pre_save, sender=song)
def artirest(sender, instance, **kwargs):
    if instance.album:
        instance.artirst=instance.album.artirst

