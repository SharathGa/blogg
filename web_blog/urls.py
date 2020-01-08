from django.urls import path

from . import views  # importing the logic

urlpatterns = [
    path("", views.home, name="blog-home"),
    path("about/", views.about, name="blog-about"),
]
