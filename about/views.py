from django.shortcuts import render


def about(request):
    """ A view to return the About Page """
    return render(request, 'about/about.html')
