from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q
from .models import Product, ProductFeature, Category
from .forms import ProductForm, ProductFeatureForm

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


@staff_member_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@staff_member_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@staff_member_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product successfully deleted!')
    return redirect(reverse('products'))


@staff_member_required
def add_feature(request):
    """ Add a product feature to the db """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductFeatureForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request, 'Successfully added product feature!')
            return redirect(reverse('add_feature'))
        else:
            messages.error(request, 'Failed to add product featured. Please ensure the form is valid.')
    else:
        form = ProductFeatureForm()

    template = 'products/add_feature.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@staff_member_required
def edit_feature(request, feature_id):
    """ Edit a product feature """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    feature = get_object_or_404(ProductFeature, pk=feature_id)
    if request.method == 'POST':
        form = ProductFeatureForm(request.POST, request.FILES, instance=feature)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated feature!')
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Failed to update feature. Please ensure the form is valid.')
    else:
        form = ProductFeatureForm(instance=feature)
        messages.info(request, f'You are editing {feature.name}')

    template = 'products/edit_feature.html'
    context = {
        'form': form,
        'feature': feature,
    }

    return render(request, template, context)


@staff_member_required
def delete_feature(request, feature_id):
    """ Delete a product feature from the db """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    feature = get_object_or_404(ProductFeature, pk=feature_id)
    feature.delete()
    messages.success(request, 'Product feature successfully deleted!')
    return redirect(reverse('products'))
