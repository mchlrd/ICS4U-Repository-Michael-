from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from csf12 import settings
from django.core.mail import send_mail

def home(request):
    return render(request, 'index.html')
def signup(request):

    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if User.objects.filter(username = username):
            messages.error(request, "This username already taken")
            return redirect('home')
        
        if User.objects.filter(email = email):
            messages.error(request, "This email already taken")
            return redirect('home')
        
        if len(username) > 10:
            messages.error(request, "Username is too long (< 10)")

        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            

        if not username.isalnum():
            messages.error(request, "The username must be alpha-numeric")
            return redirect('home')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your account has been successfully created. Check your email.")

        #Welcome Email

        subject = "Welcome to the Alpha Test"
        message = "Hello " + myuser.first_name + ".\n" + "Welcome to our Alpha Test\nThank you for visiting our webiste\n\n Sincerely,\nDeveloper Team"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject,message,from_email,to_list, fail_silently=True)
        return redirect('signin')
    
    return render(request, 'signup.html')

def signin(request):

    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "index.html", {'fname': fname})

        else:
            messages.error(request, "Wrong Credentials")
            return redirect('home')

    return render(request, 'signin.html')

def signout(request):
    logout(request)
    messages.success(request, "You are now logged out")
    return redirect('home')