from django.db import models

class Movie(models.Model):
    imdb_title_id = models.CharField(max_length=64, primary_key=True)
    title = models.CharField(max_length=512)
    description = models.TextField()
    director = models.CharField(max_length=1024)

    def __str__(self):
        return f'{self.title}'

    