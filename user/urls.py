# ---------------------------------------------------------------------------- TECHBOY/HOME/URLS.PY
from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user, name='user'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
