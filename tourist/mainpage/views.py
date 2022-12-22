from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "num_okno" : 789,
        'per1' : "коллекции"
        

    }
    return render(
        request,              # Запрос
	'mainpage/index.html', # путь к шаблону
    context                # подстановки
    ) # путь к шаблону
