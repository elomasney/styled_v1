from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, ProductFeature
from .forms import GiftVoucherForm

# Create your views here.


def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()
    query = None

    if request.GET:
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
    """ A view to return the Gift Vouchers Page """
    gift_voucher_form = GiftVoucherForm()

    context = {
        'gift_voucher_form': gift_voucher_form,
    }

    return render(request, 'products/gift_voucher.html', context)
