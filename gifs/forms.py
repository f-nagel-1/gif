from django import forms
from .models import Gifs

class GifForms(forms.ModelForm):
    class Meta:
        model = Gifs
        fields = [
            'title',
            'url',
            'uploader_name',
            'created_at'
        ]