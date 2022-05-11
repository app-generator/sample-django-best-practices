from django.urls import path, re_path

from apps.home import views

urlpatterns = [
    # The home page
    path("", views.index, name="index"),
    # Matches any html file
    path("home", views.home, name="home"),

]

