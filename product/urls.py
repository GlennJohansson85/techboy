#----------------------------------------------------------------------------    TECHBOY/PRODUCT/URLS.PY
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list_view, name='product_list_view'),
    path('<int:product_id>/', views.product_detail_view, name='product_detail_view'),
    path('add/', views.product_add_view, name='product_add_view'),
    path('edit/<int:product_id>/', views.product_edit_view, name='product_edit_view'),
    path('delete/<int:product_id>/', views.product_delete_view, name='product_delete_view'),
]
