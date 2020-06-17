from django.db import models
from django.contrib.auth.models import User
# from django.contrib.postgres.fields import ArrayField


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


class Comentario(models.Model):
    content = models.CharField(max_length=50)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    movie = models.CharField(max_length=50)

    def __str__(self):
        return 'Comentario de '+ self.user.username + ' en ' + self.movie
    
