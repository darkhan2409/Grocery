from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView, name='home_url'),
    path('about_us', aboutUsView, name='about_us_url'),
    path('sign_in', signInView, name='sign_in_url'),
    path('sign_up', signUpView, name='sign_up_url'),
    path('sign_out', signOutView, name='sign_out_url'),
]