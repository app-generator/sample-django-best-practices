from django.template import loader, TemplateDoesNotExist
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    context = {"segment": "index"}

    html_template = loader.get_template("index.html")
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def home(request):
    context = {
        "user": request.user
    }

    html_template = loader.get_template("accounts/home.html")
    return HttpResponse(html_template.render(context, request))
