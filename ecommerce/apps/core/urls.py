from unicodedata import name
from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path('', views.frontpage, name="frontpage"),
    path('contact/', views.contact, name="contact")
]