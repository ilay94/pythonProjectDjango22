from django.shortcuts import render

# Create your views here.


def home(request):
    """Контроллер отображения домашней страницы"""
    return render(request, "home.html")


def contacts(request):
    """Контроллер отображения страницы контактов"""
    return render(request, "contacts.html")
