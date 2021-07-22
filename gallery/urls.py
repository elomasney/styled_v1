from django.urls import path
from . import views

urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
    path('add/', views.add_image, name='add_image'),
]
