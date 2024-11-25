from django.shortcuts import render
from Musician_app.models import Musician
from Album_app.models import Album

def home(request):
    albums = Album.objects.all()
    return render(request, 'home.html', {'albums' : albums})