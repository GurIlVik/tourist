from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(
        request,              # Запрос
	'mainpage/index.html', # путь к шаблону
    context                # подстановки
    ) # путь к шаблону
