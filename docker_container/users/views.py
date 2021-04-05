from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST': 
        userForm = UserCreationForm(request.POST)
        if userForm.is_valid():
            print("VALIDNESS-------------------------------------------------")
            form.save()
            username = userForm.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/integration/')

    else: 
        userForm = UserCreationForm()
    print("not having a good time-------------------------------------------------")
    return render(request, 'users/register.html', {'userForm' : userForm})
    
