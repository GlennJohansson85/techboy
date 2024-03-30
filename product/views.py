from django.shortcuts import render, redirect, reverse
from .models import Product


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'product/product_list_view.html',)


def product_detail_view(request, product_id):
    return render(request, 'product/product_detail_view.html',)


def product_add_view(request):
    return render(request, 'product/product_add_view.html',)


def product_edit_view(request, product_id):
    return render(request, 'product/product_edit_view.html',)


def product_delete_view(request, product_id):
    return reverse(request, 'product/product_delete_view.html',)
