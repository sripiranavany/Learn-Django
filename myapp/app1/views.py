from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages, auth

from .models import Feature


# Create your views here.
def index(request):
    # return render(request, 'app1/index.html')
    # return HttpResponse("Hello, world. You're at the app1 index.")
    # context = {
    #     'name': 'Sripiranavan',
    #     'age': 25,
    #     'nationality': 'Sri Lankan'
    # }

    context = Feature.objects.all()
    return render(request, 'index.html', {'context': context})


def counter(request):
    posts = [1, 2, 3, 4, 5]
    return render(request, 'counter.html', {'posts': posts})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email)
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'login.html')


def logout(request):
    if request.method == 'POST' or 'GET':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

def post(request, pk):
    return render(request, 'post.html', {'pk': pk})