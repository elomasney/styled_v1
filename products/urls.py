from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),
    path('feature/', views.add_feature, name='add_feature'),
    path('edit_feature/<int:feature_id>/', views.edit_feature,
         name='edit_feature'),
    path('delete_feature/<int:feature_id>/', views.delete_feature,
         name='delete_feature'),
]
