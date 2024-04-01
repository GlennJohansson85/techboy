#----------------------------------------------------------------------------TECHBOY/PRODUCT/URLS.PY
from django.urls import path
from . import views

urlpatterns = [
    path('',views.products,name='products'),
    path('<int:product_id>/',views.product_detail,name='product_detail'),
    path('add/',views.product_add,name='product_add'),
    path('edit/<int:product_id>/',views.product_edit,name='product_edit'),
    path('delete/<int:product_id>/',views.product_delete,name='product_delete'),
]