from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == 'POST': 
        userForm = UserRegisterForm(request.POST)
        if userForm.is_valid():
            userForm.save()
            username = userForm.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Please log in!')
            return redirect('/login/')

    else: 
        userForm = UserRegisterForm()
    return render(request, 'users/register.html', {'userForm' : userForm})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
