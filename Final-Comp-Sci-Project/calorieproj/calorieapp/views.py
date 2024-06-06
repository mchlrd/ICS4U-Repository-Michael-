from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def calorieCounter(request):
    import requests
    import json

    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query, headers={'X-Api-Key': 'odTlIxnB1iALO6X+LUUqTw==ZL5tL1eOQewHLIbV'})
        print(api_request.content)
        try:
            api = json.loads(api_request.content)
            if isinstance(api, list) and len(api) > 0:
                api = api[0]
            else:
                api = 'No results found.'
        except Exception as e:
            api = 'Oops... There is an error ^_^'
            print(e)
        return render(request, 'calorieCounter.html', {'api': api})
    else:
        return render(request, 'calorieCounter.html', {'api': None})

def homepage(request):
    return render(request, 'homepage.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('calorieCounter')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('calorieCounter')
            else:
                messages.info(request, 'Username or Password is incorrect')
        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('calorieCounter')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was created for " + user)
                return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)
