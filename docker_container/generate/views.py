from django.shortcuts import render, get_object_or_404
from .models import Pizza, Topping


# Create your views here.

def index(request):
    all_pizza = Pizza.objects.all()
    return render(request, 'generate/index.html', {'all_pizza' : all_pizza})

###Shorter Shortcut version of the above
# from django.shortcuts import render
# def index(request):
#     all_pizza = Pizza.objects.all()
#     context = {'all_pizza': all_pizza}
#     return render(request, 'generate/index.html', context)

def detail(request, pizza_id):
    all_pizza = Pizza.objects.all()
    pizza = get_object_or_404(Pizza, id=pizza_id)
    return render(request, 'generate/detail.html', {
    'pizza': pizza,
    'all_pizza' : all_pizza
    })

def nutrition(request):
    return render(request, 'generate/nutrition.html', {})
