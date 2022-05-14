from django.contrib.auth import authenticate, login
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from ratelimit.decorators import ratelimit

from apps.user.models import User
from .forms import LoginForm, SignUpForm


@ratelimit(key="ip", rate="10/5m", method=ratelimit.ALL, block=True)
def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                try:
                    user_temp = User.objects.get(username=username)
                except ObjectDoesNotExist:
                    user_temp = None

                if user_temp is None:
                    msg = "This account doesn't exist."
                else:
                    msg = "Invalid credentials"
        else:
            msg = "Error validating the form"

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


@ratelimit(key="ip", rate="10/5m", method=ratelimit.ALL, block=True)
def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form_kwargs = {"domain": get_current_site(request).domain}
            form.save(**form_kwargs)

            success = True

            msg = 'User created - please <a href="/login">login</a>.'

        else:
            msg = "Form is not valid"
    else:
        form = SignUpForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form, "msg": msg, "success": success},
    )
