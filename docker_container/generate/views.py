import json
from django.shortcuts import render, get_object_or_404
from . models import Pizza, Topping
from . serializers import PizzaSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

#integration
from subprocess import run, PIPE



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

def form(request):
    return render(request, 'generate/form.html', {})

########## For Inegration Below 
def integration(request):
    return render(request, 'generate/integration.html')

def external(request):
    ingredient = request.POST.get
    recommendation = run([sys.executable, "..//..//PizzeriaMLcode.py", ingredient], shell=False, stdout=PIPE)
    print(recommendation)

    return render(request, 'integration.html', {'ingredient1':ingredient})
    



########### For Integration Above
@api_view(['GET'])
def getAllPizza(request):
    pizza = Pizza.objects.all()
    serializer = PizzaSerializer(pizza, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPizza(request, id):
    pizza = Pizza.objects.get(id=id)
    serializer = PizzaSerializer(pizza, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createPizza(request):
    pizza = PizzaSerializer(data=request.data)

    if pizza.is_valid():
        pizza.save()

    return Response(pizza.data)
