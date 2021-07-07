from django.shortcuts import render


def index(request):
    """ A view to return the Homepage """
    return render(request, 'home/index.html')
