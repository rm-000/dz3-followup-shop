Новый проект
пипи инстол джанго
новый проектран сервер
создать views.py		(отвечает за функции, которые выполняются при заходе на конкретную страницу)

views:
from django.http import HttpResponse

def main_page(request):
    text = '<h1>Main Page</h1>'
    return HttpResponse(text)
	
urls:
from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page),
]


Исправить views:

from django.http import HttpResponse
from django.shortcuts import render

def main_page(request):
    text = '<h1>Main Page</h1>'
    return render(request, "./index.html")
	

Создать в корне директорию templates
там создать index.html

Изменить во views:
text_html = '<h2>Main Page</h2>'

Указать джанго откуда брать шаблоны:
settings.py - TEMPLATES - DIRS:
        'DIRS': [ BASE_DIR / 'templates' ],
		
Изменить views и создать словарь, в котором создам переменные, которые передам в этот шаблон

def main_page(request):
    text_html = '<h2>Subtitle</h2>'
    just_text = 'Hello'
    return render(request, "./index.html", {
        'string1': text_html
        'string2': just_text
        'string3': 'static text'
    })

	# string 1,2,3 - Это переменные. Стринг3 - для примера показать, что может передаваться строка
	
	# создавая параметры в словаре и передавая его шаблону, мы получаем параметры с динамическим контентом.
	
Как в html вставить параметры из словаря? - применяем nfr так называемую Директиву {{ }}:

<body>
    <h1>Main Page</h1>
    <ul>
        <li> {{ string1 }} </li>
        <li> {{ string2 }} </li>
        <li> <h2> {{ string3 }} </h2> </li>
    </ul>
</body>

На странице index.html оформление переменных не сохранится:
def main_page(request):
    text_html = '<h2>Subtitle</h2>'
	
	# текст_хтмл отобразится просто текстом с тегами, а не с выделением подзаголовка 2 уровня. - это защита от хацкеров.
	
	Чтобы сработало оформление, то его нужно делать не во views, Где задаются переменные, а в Index.html:
	#        <li> <h2> {{ string3 }} </h2> </li>
	
во вьюс меняю детальный словарь на переменную context, обозначающую словарь. Создаю разделы сайта [список]. Создаю {словари}. Создаю вывод словаря:

def main_page(request):
    menu = ['главная', 'каталог', 'о сайте']
    dict = {'name': 'Ivan', 'age': 23}
    browser = request.META['HTTP_USER_AGENT']
    data = {'menu':menu, 'user':dict, 'browser':browser}
    return render(request, "./index.html", context = data)
	
Меняю индекс.хтмл:

<body>
    <h1>Main Page</h1>
    <ul>
        <li> {{ menu }} </li>
        <li> {{ user }} </li>
        <li> {{ browser }} </li>
    </ul>
</body>

Чтобы обратиться к одному из элементов списка, нужно через точку написать порядковый номер эл-та в списке. Чтобы вывести эл-т словаря, нужно написать его имя:

<body>
    <h1>Main Page</h1>
    <ul>
        <li> {{ menu.1 }} </li>
        <li> {{ user.name }} </li>
        <li> {{ browser }} </li>
    </ul>
</body>

Но это выведение по одному элементу СПИСКА. А если выводить много, то нужн цикл. Для этого используем директиву {% for i in list %} ... {% endfor %}. Это выведет все элементы, например, СПИСКА Меню.

<body>
    <h1>Main Page</h1>
    <ul>
        {% for i in menu %}
        <li> {{ i }} </li>
        {% endfor %}
    </ul>
</body>


Если в списке ничего нет, то ничего не выведется. А если все же нужно предупредить пользователя, что что-то должно быть, но здесь пусто, то используем другую директиву:

во вьюс:
def main_page(request):
    menu = []

в индекс.хтмл:
    <ul>
        {% for i in menu %}
        <li> {{ i }} </li>
        {% empty %}
        <li> Нет элементов </li>
        {% endfor %}
    </ul>


Проделаем то же для СЛОВАРЯ. Поменяем main и вставим туда ссылки на страницы:

def main_page(request):
    menu = {'главная':'/', 'каталог':'/catalog', 'о сайте':'/about'}
    dict = {'name': 'Ivan', 'age': 23}
    data = {'menu':menu, 'user':dict}
    return render(request, "./index.html", context = data)

    <ul>
        {% for key, value in menu.items %}
        <li><a href="{{ value }}">{{ key }}</a></li>
        {% empty %}
        <li> Нет элементов </li>
        {% endfor %}
    </ul>	

	#key, value - переменные. Их названия - любые. Обращение к элементу списка через .items
	
	
Рассмотрим другие директивы
Вернем меню как список. Выведем его элементы.
Чтобы вывести порядковый номер элемента списка и его значение, делаем так:

    menu = ['главная', 'каталог', 'о сайте']
	
чтобы обратиться к переменной внутри цикла, используем пространство имен forloop.
обратимся к существующей в джанго/питоне переменной "counter":

    <ul>
        {% for value in menu %}
        <li>{{ forloop.counter }} {{ value }} </a></li>
        {% endfor %}
    </ul>
	
Отсчет начнется с единицы. Если нужно начать отсчет с нуля, то нужно использовать переменную counter0.

Есть еще другие переменные. Можно вывести элементы в списке в обратном порядке. Нужно после имени перечисляемой переменной menu написать "reversed":
        {% for value in menu reversed %}
		Получится:
			1 о сайте
			2 каталог
			3 главная
		Чтобы поменялись не только элементы списка, но и порядковые номера, используем переменную revcounter (есть также revcounter0):

    <ul>
        {% for value in menu reversed %}
        <li>{{ forloop.revcounter }} {{ value }} </a></li>
        {% endfor %}
    </ul>
	
	
Рассмотрим еще директиву - if. Сделаем ветвление.
Если переменная меню содерит данные [Главная, каталог, о нас], то выведется список элементов меню. Если список меню пуст (Menu = []), то выведется пусто

    menu = ['главная', 'каталог', 'о сайте']
	
    <ul>
        {% if menu%}
            {% for value in menu %}
            <li>{{ value }}</li>
            {% endfor %}
        {% else %}
            <li>пусто</li>
        {% endif %}
    </ul>
	

Создадим демо интернет-магаз со страницами: главная, каталог, о нас. 

Urls:

urlpatterns = [
    path('', main_page),
    path('catalog', catalog_page),
    path('about', about_page),
]

	#Если будет просто path('', catalog_page),  то при переходе по ссылке на /catalog страница существовать не будет. То есть я делаю вывод, что 'catalog' - название страницы, а catalog_page - функция, которая обрабатывает отображение страницы.


Views:

переменную меню вынесем из функции и напишем большими, чтобы обратить внимание читающего, что это глобальная функция. Создадим перем. заголовка title. Создадим функции для других страниц:

MENU = ['главная', 'каталог', 'о сайте']

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
	
	
Создадим шаблон в корневой папке для типовой страницы сайта - base.html. Страница содержит части: Header, sidebar, content. Каждой части назначим одноименный класс, а также добавим класс item (два класса пишутся через пробел)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
</head>
<body>
    <div class="container">
        <div class="header item">
            Header
        </div>
        <div class="sidebar item">
            <ul>
                {% for key, value in menu.items %}
                <li><a href='{{ value }}'>{{ key }}</a></li>
                {% endfor %}
            </ul>
        </div>
        <div class="content item">
            {% block content %}
            {% endblock %}
        </div>
    </div>
</body>
</html>

В индекс.хтмл напишем директиву {%%}, открывающую base.html.
Далее нужно вставить блок и назвать его (block content), в нем поместить какое-то содержимое. Закрыть блок:

{% extends 'base.html'%}

{% block content %}
<h1>{{ title }}</h1>

<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet aperiam assumenda at consequuntur cumque delectus eos exercitationem fuga hic, id illo incidunt, ipsa iste necessitatibus nisi obcaecati officia sed temporibus?</p>

{% endblock %}


Добавляем страницы хтмл about (копипаста index):

{% extends 'base.html'%}

{% block content %}
<h1>{{ title }}</h1>

<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet aperiam assumenda at consequuntur cumque delectus eos exercitationem fuga hic, id illo incidunt, ipsa iste necessitatibus nisi obcaecati officia sed temporibus?</p>

{% endblock %}


Добавляем хтмл catalog, поменяем чуть структуру:

{% extends 'base.html'%}

{% block content %}
<h1>{{ title }}</h1>

<ul>
    <li>продукт 1</li>
    <li>продукт 2</li>
    <li>продукт 3</li>
    <li>продукт 4</li>
    <li>продукт 5</li>
</ul>

{% endblock %}


Далее подключим стили.

В Джанго: "Статические файлы" - это css, javascript, фото и видео.

Для этого нужно создать в корне папку 'static'. По-хорошему разделить там папки в соответствии с контентом (css, js, фото, видео...).
Для текущей задачи создадим только папку 'css'. В ней создадим файл base.css

В Папке настроек создать новую переменную после переменной 'STATIC_URL':
STATICFILES_DIRS = [ BASE_DIR / 'static' ]

#так же, как когда добавлял папку 'templates'


Напишем содержимое base.css:

.container {
    display: grid;					#чтобы выравнивалось по рядам
    grid-template-areas:			#какое место назначить каждому элементу в пропорциях друг друга
        'header header';
        'sidebar content';
    gap: 10px;						#расстояние между Header, sidebar, content
    grid-template-columns: 150px, 1fr;
    grid-template-rows: 50px, 1fr;
}

.header {
    grid-area: header;
}

.sidebar {
    grid-area: sidebar;
    align-self: start;
}

.content {
    grid-area: content;
}

.item {
    border: 1px solid black;
    padding: 5px;
}


Подключаем стиль css к сайту через изменение base.html:

{% load static %}		#эта директива позволяет подключать статический контент (css, js, фотовидео)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="{% static 'css/base.css' %}">		#так указывается путь к файлу стилей
</head>