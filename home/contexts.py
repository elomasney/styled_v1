from django.shortcuts import get_object_or_404
from products.models import Product, Category
from gallery.models import Image, Collection


def navbar_options(request):
    category = get_object_or_404(Category, pk=1)
    products = Product.objects.filter(category=1)
    collections = Collection.objects.all()
    images = Image.objects.filter(collection__name__in=collections)

    context = {
        'products': products,
        'category': category,
        'collections': collections,
        'images': images,

    }
    return context
