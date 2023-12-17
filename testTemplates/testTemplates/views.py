from django.http import HttpResponse
from django.shortcuts import render

MENU = {'главная':'/', 'каталог':'/catalog', 'о сайте':'/about'}

def main_page(request):
    title = 'Главная страница'
    data = {'menu':MENU, 'title':title}
    return render(request, "./index.html", context = data)

def catalog_page(request):
    title = 'Каталог'
    data = {'menu':MENU, 'title':title}
    return render(request, "./catalog.html", context = data)

def about_page(request):
    title = 'О компании'
    data = {'menu':MENU, 'title':title}
    return render(request, "./about.html", context = data)