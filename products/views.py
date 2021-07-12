from django.shortcuts import render, get_object_or_404
from .models import Product, ProductFeature
from .forms import GiftVoucherForm

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
