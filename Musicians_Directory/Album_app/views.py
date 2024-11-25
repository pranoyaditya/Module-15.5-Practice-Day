from django.shortcuts import render,redirect
from .forms import AlbumForm
from .models import Album

# Create your views here.
def add_album(request):
    if request.method == 'POST':
        albumForm = AlbumForm(request.POST)
        if albumForm.is_valid():
            albumForm.save()
            return redirect('HomePage')
    else:
        albumForm = AlbumForm()
    return render(request, 'Album_app/addAlbum.html', {'albumForm' : albumForm})

def edit_album(request,id):
    albumData = Album.objects.get(pk=id)
    albumForm = AlbumForm(instance=albumData)
    if request.method == 'POST':
        albumForm = AlbumForm(request.POST, instance=albumData)
        if albumForm.is_valid():
            albumForm.save()
            return redirect('HomePage')
    return render(request, 'Album_app/addAlbum.html', {'albumForm' : albumForm})

def delete_album(request,id):
    albumData = Album.objects.get(pk=id)
    albumData.delete()
    return redirect('HomePage')