from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings


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


def send_contact_form(request):
    """ Send contact form to company email address """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = render_to_string(
                'home/contact_emails/contact_form_subject.txt',
                {'subject': form.cleaned_data['subject']})
            message = render_to_string(
                'home/contact_emails/contact_form_message.txt',
                {'message': form.cleaned_data['message'],
                 'email': form.cleaned_data['email']})

            try:
                send_mail(
                    subject, message,
                    settings.DEFAULT_FROM_EMAIL, ['styledv1@gmail.com']
                    )
            except BadHeaderError:
                messages.warning(request, 'An error occured. Please try again')

            context = {
                'form': form,
            }

        return render(request, 'home/thank_you.html', context)
