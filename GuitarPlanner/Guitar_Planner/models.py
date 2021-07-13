from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.



class Exercise(models.Model):

    # Model of 'Exercise' objects.

    name = models.CharField(max_length=64)
    description = models.CharField(max_length=2000)
    speed = models.IntegerField(null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)


class Band(models.Model):

    # Model of 'Band' objects.

     name = models.CharField(max_length=500)
     year_of_creation = models.IntegerField(null=True)
     user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

class Song(models.Model):

    # Model of 'Song' objects.

    name = models.CharField(max_length=500)
    genre = models.CharField(max_length=500)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

class Back_log(models.Model):

    # Model of 'Song' objects.

    name = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    value = models.IntegerField(null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

class Month(models.Model):

    # Model of 'Song' objects.

    name = models.CharField(max_length=64)
    year = models.IntegerField(null=False)
    exercise = models.ManyToManyField(Exercise)
    song = models.ManyToManyField(Song)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)



