#------------------------------------------------------------------------------PRODUCT/VIEWS.PY
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product


def product_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    products = Product.objects.filter(category=category)

    return render(request, 'product/product_category.html', {'category': category, 'products': products})


def products(request):
    """ A view to show all products """
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'product/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'product/product_detail.html', {'product': product})


def product_add(request):
    """ A view to add a new product """
    # Assuming you have a form defined for adding products
    form = None
    template = 'product/product_add.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def product_edit(request, product_id):
    """ A view to edit an existing product """
    # Assuming you have a form defined for editing products
    form = None
    product = get_object_or_404(Product, pk=product_id)
    template = 'product/product_edit.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


def product_delete(request, product_id):
    """ A view to delete an existing product """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    # Assuming you're using Django's messages framework
    from django.contrib import messages
    messages.success(request, 'Product deleted!')

    return redirect('products')
