from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def home(request):
    return render(request, 'hotel_bristol/home.html', {'title': 'Главная страница'})


def rent(request):
    pass


def about(request):
    pass


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Данная страница не существует</h1>")


