# Создание блога на Джанго

## Подготовка 

### Создание виртуального окружения

На WIN жмем WIN+R для загрузки командной строки либо заходим через пуск\поиск

Набираем 'cmd' (тем самым вызывая командную строку)

Cоздаем папку проекта в открывшемся окне командой * md C:\Name

Переходим в папку проекта командой * cd C:\Name

В папке проекта создаем VENV командой * python -m venv venv (для MAC\LINUX * python3 -m venv venv)

Активируем VENV командой * venv\Scripts\activate (для MAC\LINUX * source venv/bin/activate)

Проверяем установленные библиотеки командой * pip list

Если необходимо обновляем сам pip командой * python.exe -m pip install --upgrade pip

Для выхода из виртуального окружения команда * deactivate

### Работа в среде разработки
Для данного урока используется PyCharm

Откройте PyCharm, создайте новый проект (New Project - Create)

Для примера назовем его 'Blog'

Войдите в терминал (слева внизу, Alt+F12) и наберите:

    pip install django

Сохраните скачанные библиотеки в файл requirements для развертки на других системах.

Напишите в терминале:

    pip freeze > requirements.txt

Запустите панель администратора Джанго. Наберите в терминале:

    django-admin.exe startproject djangoshop

## Создание блога и отдельных страниц

### Работа с файлом views.py

В папке Blog создайте файл views.py (отвечает за функции, которые выполняются при заходе на конкретную страницу)

В содержании views.py напишите следующее:

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

### Работа с urls.py

Введите следующее содержимое:

    from .views import *

    urlpatterns = [
        path('', main_page),
        path('about/', about_page),
        path('article1/', article1),
        path('article2/', article2),
        path('article3/', article3),

### Создание страниц сайта
Создайте в корне директорию templates

В ней создайте файлы т.н. шаблоны, которые Джанго будет загружать при переходе пользователя по определенным ссылкам:

index.html, base.html, article1.html, article2.html, article3.html, about.html

index - это главная страница сайта

base - шаблон, который будет применяться ко всем страницам сайта

article 1,2,3 - страницы статей блога

about - страница с информацией о блоге

___
#### Пример содержания указанных выше файлов можете посмотреть здесь:
    https://всессылкитут...
___

### Работа с settings.py
Далее необходимо указать Джанго откуда брать шаблоны:

В файле settings.py находим строчку TEMPLATES, в ней указываем содержание для 'DIRS':
        
    'DIRS': [ BASE_DIR / 'templates' ],

так же изменим параметр:

    STATICFILES_DIRS = [ BASE_DIR / 'static' ]

### Стили для сайта

В корневом каталоге создайте папку для называемых Джанго 'статичных' файлов. Папка 'static' (путь к ней мы указали в предыдущем шаге)

В папке 'static' создайте папку 'css', а в ней создайте файл 'base.css'

Для примера можно использовать такие стили:

___
#### Пример содержания файла base.css смотрите по ссылке:
    https://всессылкитут...

___
Объяснение содержания указанных файлов вы найдете здесь:

    https://всессылкитут...