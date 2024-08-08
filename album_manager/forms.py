from django import forms
from .models import Album, Artist

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), 
            'height': forms.DateInput(attrs={'class': 'form-control'}),
            'genre' : forms.Select (attrs={'class': 'form-control'}),
            'artist' : forms.Select (attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        } 

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
        widgets = {
            'artist_name':forms.TextInput(attrs={'class' : 'form-control'}),
            'country':forms.TextInput(attrs={'class' : 'form-control'}),
        }