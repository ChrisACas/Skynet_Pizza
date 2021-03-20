from django import forms


class command_form(forms.Form):
    command = forms.CharField(max_length=200)