import json
import sys
from django.shortcuts import render, get_object_or_404
from . models import Pizza, Topping
from . serializers import PizzaSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

#integration
from subprocess import run, PIPE, Popen
from  . forms import command_form



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
    ingredient = request.POST.get('param1')
    print(ingredient)
    MLoutput = run([sys.executable, "/Users/engrbundle/Documents/ECEN 404/Skynet_Pizza/PizzeriaMLcodeModified.py", ingredient], shell=False, stdout=PIPE)
    recommendation = MLoutput.stdout.decode("utf-8").replace('/n', '  |  ')
    print(recommendation)

    return render(request, 'generate/integration.html', {'ingredient1':recommendation})
    

# def welcome_page(request):
    output = ""
    # Initialize the form. At this point you have an unbound/invalid form
    myform = command_form()  # better write it as CommandForm

    if request.method == "POST":
        myform = command_form(request.POST)
        if myform.is_valid():
            # execute_command variable, should now contain the command typed by the user in the text box
            execute_command = myform.cleaned_data['command']
            try:
                # If the return code is non-zero, CalledProcessError will be raised
                output = sp.Popen(execute_command, shell=True)
            except sp.CalledProcessError:
                exit_code, error_msg = output.returncode, output.output
    return render(request, 'generate/integration.html', locals())



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
