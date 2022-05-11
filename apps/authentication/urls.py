# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path

from apps.authentication.views import login_view, register_user

urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register_user, name="register")
]
