from django.shortcuts import render

from .forms import GifForms

# Create your views here.

def gif_form(request):
    form = GifForms(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'form.html', {'form':form})
