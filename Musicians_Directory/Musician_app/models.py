from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)  # Enforce unique emails for musicians
    phone = models.CharField(max_length=12, blank=True, null=True)  # Allow optional phone numbers
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.instrument}"

