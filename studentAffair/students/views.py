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

def viewConfirm(request, pk):
    student = Student.objects.get(id = pk)
    if request.method == 'POST' :
        if student.status == 'Active':
            Student.objects.filter(id = pk).update(status = "InActive")
        else:
            Student.objects.filter(id = pk).update(status = "Active")
        return redirect('/')

    context = {'student':student}
    return render(request, 'students/viewConfirm.html', context)


def delete(request):
    context = {'students':Student.objects.all()}
    return render(request,'students/delete.html',context)


def deleteConfirm(request, pk):
    student = Student.objects.get(id = pk)
    if request.method == 'POST' :
        student.delete()
        return redirect('/')

    context = {'student':student}
    return render(request, 'students/deleteConfirm.html', context)


