from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, ProductFeature, Category

# Create your views here.


def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    features = ProductFeature.objects.filter(product=product_id)

    context = {
        'product': product,
        'features': features,
    }

    return render(request, 'products/product_detail.html', context)


def gift_voucher(request):
    category = get_object_or_404(Category, pk=2)
    giftvouchers = Product.objects.all()

    context = {
        'category': category,
        'giftvouchers': giftvouchers,
    }

    return render(request, 'gift_voucher.html', context)
