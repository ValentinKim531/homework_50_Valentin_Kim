from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def index_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'index.html')
