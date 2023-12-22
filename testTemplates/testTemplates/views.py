from django.http import HttpResponse
from django.shortcuts import render

MENU = {'главная':'/', 'о блоге':'/about'}

def main_page(request):
    title = 'Блог'
    data = {'menu':MENU, 'title':title}
    return render(request, "./index.html", context = data)

def about_page(request):
    title = 'О блоге'
    data = {'menu':MENU, 'title':title}
    return render(request, "./about.html", context = data)

def article1(request):
    title = 'Статья 1'
    data = {'menu':MENU, 'title':title}
    return render(request, "./article1.html", context = data)

def article2(request):
    title = 'Статья 2'
    data = {'menu':MENU, 'title':title}
    return render(request, "./article2.html", context = data)

def article3(request):
    title = 'Статья 3'
    data = {'menu':MENU, 'title':title}
    return render(request, "./article3.html", context = data)