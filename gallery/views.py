from django.shortcuts import render
from .models import Image, Collection


# Create your views here.
def gallery(request):
    """ A view to return the Gallery Page"""
    images = Image.objects.all()
    collections = None

    if request.GET:
        if 'collection' in request.GET:
            collections = request.GET['collection'].split(',')
            images = images.filter(collection__name__in=collections)
            collections = Collection.objects.filter(name__in=collections)

    context = {
        'images': images,
        'current_collections': collections
    }
    return render(request, 'gallery/gallery.html', context)
