#----------------------------------------------------------------------------TECHBOY/TECHBOY/URLS.PY
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('allauth.urls')),
    path('', include('home.urls')),
    path('', include('user.urls')),
    path('product/', include('product.urls')),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



