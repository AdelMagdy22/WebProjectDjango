from django.shortcuts import render
# from django.http import HttpRequest, HttpResponse
# Create your views here.

# def home():
#     return render(request , 'pages\main page.html.')

def home(request):
    return render(request,'pages/mainPage.html')

def addStudent(request):
    return render(request,'pages/addstudent.html')

def delete(request):
    return render(request,'pages/delete.html')

def DepartmentAssignment(request):
    return render(request,'pages/DepartementAssignmentPage.html')

def login(request):
    return render(request,'pages/login.html')

def tutorial(request):
    return render(request,'pages/MyTutorialPage.html')

def search(request):
    return render(request,'pages/Search.html')

def updatehomepage(request):
    return render(request,'pages/UpdateHomePage.html')

def update(request):
    return render(request,'pages/UpdateInfo.html')

def view(request):
    return render(request,'pages/view.html')