from django.db import models
from Musician_app.models import Musician

class Album(models.Model):
    album_name = models.CharField(max_length=50)
    album_release_date = models.DateField()

    RATING_CHOICES = [
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES)  # Stores the rating as an integer

    Musician = models.ForeignKey(Musician, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.album_name} by {self.Musician.first_name}'