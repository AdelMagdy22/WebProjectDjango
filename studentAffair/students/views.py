from django.shortcuts import render,redirect
from .models import Student
from .filters import StudentFilter

# Create your views here.
def search(request):
    student = Student.objects.all().exclude(status = 'InActive')

    searchFilter = StudentFilter(request.GET, queryset=student)
    student = searchFilter.qs

    context = {'students':student, 'searchFilter':searchFilter}
    return render(request,'students/Search.html',context)


def view(request):
    context = {'students':Student.objects.all()}
    return render(request,'students/view.html',context)


def delete(request):
    context = {'students':Student.objects.all()}
    return render(request,'students/delete.html',context)

