from django import forms
from django.forms import ModelForm, inlineformset_factory
from django.forms.models import inlineformset_factory
from generate.models import Pizza, Topping


class command_form(forms.Form):
    command = forms.CharField(max_length=200)

class PizzaForm(ModelForm):
    class Meta: 
        model = Pizza
        fields = ['user', 'crust', 'cheese', 'sauce']

ToppingFormset = inlineformset_factory(Pizza,
                                    Topping,
                                    fields=['topping'])

