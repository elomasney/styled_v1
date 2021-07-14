from django.urls import path
from . import views

urlpatterns = [
    path('bag/', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
]
