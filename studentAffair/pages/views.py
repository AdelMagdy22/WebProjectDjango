from django.shortcuts import render
# from django.http import HttpRequest, HttpResponse
# Create your views here.

# def home():
#     return render(request , 'pages\main page.html.')

def home(request):
    return render(request,'pages/mainPage.html')

def DepartmentAssignment(request):
    return render(request,'pages/DepartementAssignmentPage.html')

def login(request):
    return render(request,'pages/login.html')

def tutorial(request):
    return render(request,'pages/MyTutorialPage.html')

def updatehomepage(request):
    return render(request,'pages/UpdateHomePage.html')

def update(request):
    return render(request,'pages/UpdateInfo.html')

