from django.shortcuts import render, get_object_or_404
from .models import Product, ProductFeature

# Create your views here.


def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    features = ProductFeature.objects.all()

    context = {
        'product': product,
        'features': features,
    }

    return render(request, 'products/product_detail.html', context)
