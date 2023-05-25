from django.shortcuts import render
from students.models import Student

# Create your views here.
def addStudent(request):
    if request.method == 'POST':
        Id = request.POST.get('ID')
        Fname = request.POST.get('fname')
        Lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        level = request.POST.get('Level')
        gpa = request.POST.get('GPA')
        dob = request.POST.get('date')
        gender = request.POST.get('Gender')
        dept = request.POST.get('Departement')
        status = request.POST.get('Status')
        temp = Student(Fname,Lname, Id, level, gpa, gender, email, dob, phone, status, dept)
        temp.save()
    
    return render(request,'forms/addstudent.html')