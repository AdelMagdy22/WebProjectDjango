from django.shortcuts import render
from .models import Student

# Create your views here.
def search(request):
    return render(request,'students/Search.html',{'data':Student.objects.all().exclude(status = 'InActive')})

def view(request):
    return render(request,'students/view.html',{'data':Student.objects.all()})

def delete(request):
    return render(request,'students/delete.html',{'data':Student.objects.all()})