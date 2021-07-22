from django.shortcuts import render
from .forms import ContactForm


def index(request):
    """ A view to return the Homepage """
    return render(request, 'home/index.html')


def contact(request):
    """ A view to return the contact page"""
    contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'home/contact.html', context)
