from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import LoginForm


def available_apps(request):
    user = request.user
    return render(request, 'available_apps.html', {'user': user})

def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('available_apps')  # Corrected the redirect URL
        
        # form is not valid or user is not authenticated
        messages.error(request, 'Invalid username or password')
        return render(request, 'login.html', {'form': form})