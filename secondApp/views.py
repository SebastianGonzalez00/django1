from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Soy el index de app2</h1>")

def texto(request):
    html="<h1>Soy un texto 2</h1>"
    return HttpResponse(html)