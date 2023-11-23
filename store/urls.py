from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView, name='home_url'),
    path('about_us', aboutUsView, name='about_us_url'),
    path('sign_in', signInView, name='sign_in_url'),
    path('sign_up', signUpView, name='sign_up_url'),
    path('sign_out', signOutView, name='sign_out_url'),
    path('products', productsView, name='products_url'),
    path('add_to_cart/<int:product_id>', addToCartView, name='add_cart_url'),
    path('cart_detail', cartDetailView, name='cart_detail_url'),
    path('profile', profileView, name='profile_url'),
    path('products/<int:category_id>', productsByCategoryView, name='products_by_category_url'),
    path('product_detail/<int:product_id>', ProductDetailView, name='product_detail_url')
]