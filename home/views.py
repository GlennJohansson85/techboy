# ---------------------------------------------------------------------------- TECHBOY/HOME/VIEWS.PY
from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm, RegisterForm


# ---------------------------------------------------------INDEX_VIEW
def home_view(request):
    return render(request, 'home/home_view.html')


# ---------------------------------------------------------ABOUT_VIEW
def about_view(request):
    context = {
        'title': 'About Page',
        'content': 'Welcome to the About Page!',
    }
    return render(request, 'about_view.html', context)


# ---------------------------------------------------------CONTACTVIEW
def contact_view(request):
    form = ContactForm(request.POST or None)
    context = {
        'title': 'Contact',
        'content': 'Welcome to the Contact Page!',
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        return render(request, 'contact/contact_view.html', context)


# --------------------------------------------------------------------- LOGINVIEW
def login_view(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    print('User logged in')

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        print(request.user.is_authenticated)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print('ERROR')

            return render(request, 'auth/login_view.html', context)


# --------------------------------------------------------------------- REGISTERVIEW
User = get_user_model()
def register_view(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)
        print(new_user)

        return render(request, 'auth/register_view.html', context)
