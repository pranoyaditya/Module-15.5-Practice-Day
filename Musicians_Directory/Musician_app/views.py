from django.shortcuts import render, redirect
from .forms import MusicianForm
from .models import Musician

def add_musician(request):
    if request.method == 'POST':
        musician_form = MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('HomePage')
    else:
        musician_form = MusicianForm()
    return render(request, 'Musician_app/addMusician.html', {'musician_form': musician_form})

def edit_musician(reuqest,id):
    musician = Musician.objects.get(pk=id)
    musician_form = MusicianForm(instance=musician)
    if reuqest.method == 'POST':
        musician_form = MusicianForm(reuqest.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('HomePage')
    return render(reuqest, 'Musician_app/addMusician.html', {'musician_form' : musician_form})

