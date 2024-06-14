from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('reviews/<int:service_id>/', views.reviews, name='reviews'),
    ]