from django.http import HttpResponse
from django.template import loader


def index(request):
    context = {"segment": "index"}

    html_template = loader.get_template("index.html")
    return HttpResponse(html_template.render(context, request))