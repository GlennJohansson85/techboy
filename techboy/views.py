#----------------------------------------------------------------------------TECHBOY/TECHBOY/VIEWS.PY
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from .forms import ContactForm, LoginForm, RegisterForm



#---------------------------------------------------------ABOUT
def about(request):
    context = {
        'title': 'About Page',
        'content': 'Welcome to the About Page!',
    }
    return render(request, 'techboy/about.html', context)


#---------------------------------------------------------CONTACT
def contact(request):
    form = ContactForm(request.POST or None)
    context = {
        'title': 'Contact',
        'content': 'Welcome to the Contact Page!',
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'techboy/contact.html', context)


#---------------------------------------------------------LOGIN
def login(request):
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
            return render(request, 'allauth/login.html', context)


#---------------------------------------------------------REGISTER
User = get_user_model()

def register(request):
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

        return render(request, 'allauth/register.html', context)