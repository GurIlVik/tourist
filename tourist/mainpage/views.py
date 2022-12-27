from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    #template = loader.get.template('mainpage/index.html')
    context = {
        "an" : 'нечто',
               'list_1' : ['главное меню пункт1', 'главное меню пункт2', 'главное меню пункт3', 'главное меню пункт4', "главное меню пункт5", "главное меню пункт6"],
               'list_2' : ['не главное меню пункт1', 'не главное меню пункт2', 'не главное меню пункт3', 'не главное меню пункт4', 'не главное меню пункт5',],
               'list_3' : ['второстепенное меню пункт1', 'второстепенное меню пункт2', 'второстепенное меню пункт3', 'второстепенное меню пункт4', 'второстепенное меню пункт5',]
               }
    return render(
        request,              # Запрос
	'mainpage/index.html', # путь к шаблону
    context                # подстановки
    ) # путь к шаблону
