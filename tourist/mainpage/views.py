from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    #template = loader.get.template('mainpage/index.html')
    context = {'window_height':100,
               'window_widht':50,
               'Zach': ";lsdfjtghiu", 
               'list_1' : ['lsrhiu', 'laeidb', 'lseiuhgerilu']}
    return render(
        request,              # Запрос
	'mainpage/index.html', # путь к шаблону
    context                # подстановки
    ) # путь к шаблону
