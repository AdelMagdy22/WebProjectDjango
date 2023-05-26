from django.shortcuts import render

def home(request):
    return render(request,'pages/mainPage.html')

def login(request):
    return render(request,'pages/login.html')

def tutorial(request):
    return render(request,'pages/MyTutorialPage.html')