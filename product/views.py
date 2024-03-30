#----------------------------------------------------------------------------------------------PRODUCT/VIEWS.PY
from django.shortcuts import render, get_object_or_404
from .models import Product


def product_list_view(request):
    """ A view to show all products """
    products = Product.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'product/product_list_view.html', context)

def product_detail_view(request, product_id):
    """ A view to show product details """
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'product/product_detail_view.html', {'product': product})

def product_add_view(request):
    """ A view to add a new product """
    pass

def product_edit_view(request, product_id):
    """ A view to edit an existing product """
    pass

def product_delete_view(request, product_id):
    """ A view to delete an existing product """
    pass

