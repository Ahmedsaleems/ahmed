from django.urls import path
from . import views
urlpatterns = [
    path("<str:editname>", views.index, name="editpage")
]