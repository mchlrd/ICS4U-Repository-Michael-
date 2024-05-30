from django.shortcuts import render

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

def about(request):
    return render(request, 'about.html')

def support(request):
    return render(request, 'support.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')