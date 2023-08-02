from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
import requests


def home(request):
    return render(request, 'hotel_bristol/home.html')


def rent(request):
    pass


def about(request):
    pass


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Данная страница не существует</h1>")


