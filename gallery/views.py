from django.shortcuts import render
from .models import Image


# Create your views here.
def gallery(request):
    """ A view to return the Gallery Page"""
    images = Image.objects.all()

    context = {
        'images': images,
    }
    return render(request, 'gallery/gallery.html', context)
