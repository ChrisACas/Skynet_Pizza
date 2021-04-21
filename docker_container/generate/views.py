import json
import sys
from django.shortcuts import render, get_object_or_404
from . models import Pizza, Topping
from . forms import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User

import os

#integration
from subprocess import run, PIPE, Popen
from  . forms import command_form

# Create your views here.
def index(request):
    all_pizza = Pizza.objects.all()
    return render(request, 'generate/index.html', {'all_pizza' : all_pizza})
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
    # pizza_form = PizzaForm()
    # topping_formset = ToppingFormset()

    # if request.POST:
    #     pizza_form = PizzaForm(request.POST, instance=request.user)
    #     if pizza_form.is_valid():
    #         pizza = pizza_form.save()
    #         topping_formset = ToppingFormset(request.POST, instance=pizza)
    #         if topping_formset.is_valid():
    #             topping = topping_formset.save()
    #         return redirect("/profile")
    #         context = {'pizza_form': pizza_form, 'topping_formset':topping_formset}
    return render(request, 'generate/integration.html')

def external(request):
    # post requests
    crust_type = request.POST.get('crust_type')
    cheese_type = request.POST.get('cheese_type')
    sauce_type = request.POST.get('sauce_type')
    topping_num =  request.POST.get('topping_num')
    # put into one data structure (list)
    ingredients = [crust_type.split()[0].lower(), cheese_type.split()[0].lower(), sauce_type.split()[0].lower()]
    # execute script and receive feedback
    ML_path = os.path.join(os.path.dirname(__file__), 'ML/PizzeriaMLcodeModified.py')
    MLoutput = run([sys.executable,
    ML_path, 
    ' '.join(ingredients),
    str(topping_num)],
    shell=False,
    stdout=PIPE)

    raw_output = MLoutput.stdout.decode("utf-8")

    # format the output to dictionary 
    output = external_format(request, raw_output)

    #save to model
    save_recipe(request, crust_type, cheese_type, sauce_type, output)
    return render(request, 'generate/integration.html', {'output' : output})
    
def external_format(request, raw_output):
    format_string = list(filter(None, raw_output.split('\n')))
    str_list = []
    for i in format_string: 
        str_list.append(list(i.split(' ')))
        
    output_dict = dict(str_list)

    return output_dict

def piecemeal(request): 

    return render(request, 'generate/piecemeal.html')

def save_recipe(request, crust, cheese, sauce, output):
    if not request.user.is_authenticated:
        return
    pizza = Pizza()
    pizza.user = request.user
    pizza.crust = crust
    pizza.cheese = cheese
    pizza.sauce = sauce
    pizza.save()
    for k, v in output.items():
        topping = Topping()
        topping.pizza = pizza
        topping.topping = k
        topping.save()
    return


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