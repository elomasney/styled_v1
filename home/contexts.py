from gallery.models import Image, Collection
from products.models import Product, Category


def navbar_options(request):
    collections = Collection.objects.all()
    images = Image.objects.filter(collection__name__in=collections)
    services = Product.objects.filter(category=1)
    categories = Category.objects.filter(name='style_services')

    context = {
        'collections': collections,
        'images': images,
        'services': services,
        'categories': categories,
    }
    return context
