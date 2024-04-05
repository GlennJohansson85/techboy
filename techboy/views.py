#----------------------------------------------------------------------------TECHBOY/TECHBOY/VIEWS.PY
from django.shortcuts import render, redirect
from .forms import ContactForm

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