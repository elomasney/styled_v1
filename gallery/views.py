from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Image, Collection
from .forms import GalleryForm

from django.contrib.admin.views.decorators import staff_member_required


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


@staff_member_required
def add_image(request):
    """ Add a image to the gallery """
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request, 'Successfully added Gallery Image!')
            return redirect(reverse('add_image'))
        else:
            messages.error(request, 'Failed to add Gallery Image. Please ensure the form is valid.')
    else:
        form = GalleryForm()

    template = 'gallery/add_image.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
