from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    items = ["iphone", "xiomi", "sumsung"]
    return HttpResponse(items)


def contacts(request):
    return HttpResponse("<h1>Это наш Контакты: </h1>")

