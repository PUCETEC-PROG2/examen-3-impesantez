from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render
from .models import Album, Artist
from .forms import AlbumForm, ArtistForm


def index(request):
    #albums = album.objects.all() 
    albums = Album.objects.order_by('title')
    artists = Artist.objects.order_by('artist_name')
    template = loader.get_template('index.html')
    context = {
        'albums': albums,
        'artists': artists,    
        }
    return HttpResponse(template.render(context, request))

def album(request, album_id):
    album = Album.objects.get(id=album_id)
    template = loader.get_template('display_album.html')
    context = {
        'album': album,
        }
    return HttpResponse(template.render(context, request))

def artist(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    template = loader.get_template('display_artist.html')
    context = {
        'artist': artist,    
        }
    return HttpResponse(template.render(context, request))

def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = AlbumForm() 
    return render(request, 'album_form.html', {'form': form}) 


def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = ArtistForm()
    
    return render(request, 'artist_form.html', {'form': form})   

def edit_album(request, id):
    album = get_object_or_404(Album, pk = id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = AlbumForm(instance=album) 
        
    return render(request, 'album_form.html', {'form': form})  

def edit_artist(request, id):
    artist = get_object_or_404(Artist, pk = id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = ArtistForm(instance=artist)
    
    return render(request, 'artist_form.html', {'form': form})

def delete_album(request, id):
     album = get_object_or_404(Album, pk = id)
     album.delete()
     return redirect('album_manager:index')

def delete_artist(required, id):
    artist = get_object_or_404(Artist, pk = id)
    artist.delete()
    return redirect('album_manager:index')
