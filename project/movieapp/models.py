from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pelicula(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    rated = models.CharField(max_length=20)
    poster = models.CharField(max_length=40)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title