from django.shortcuts import render, redirect
from students.models import Student
from datetime import datetime

def addStudent(request):
    form = Student()
    if request.method == 'POST':
        Id = request.POST.get('ID')
        if UniqueID(Id):
            Fname = request.POST.get('fname')
            Lname = request.POST.get('lname')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            level = request.POST.get('Level')
            gpa = request.POST.get('GPA')
            dob = request.POST.get('date')
            gender = request.POST.get('Gender')
            dept = request.POST.get('Departement')
            if dept != 'CS' and dept != 'DS' and dept != 'IS' and dept != 'IT' and dept != 'AI' :
                dept = 'NULL'
            status = request.POST.get('Status') 
            form = Student(Fname,Lname, Id, level, gpa, gender, dob, email, phone, status, dept)
            form.save()
           
    return render(request,'forms/addstudent.html')


def UniqueID(SID):
    for n in Student.objects.all():
        if SID == n.id:
            return False
    return True    



def DepartmentAssignment(request, pk):
    form = Student.objects.get(id=pk)
    if request.method == 'POST':
        dep = request.POST.get('Departement')
        Student.objects.filter(id = pk).update(departement = dep)
        return redirect("/")

    context = {'form':form}
    return render(request,'forms/DepartementAssignmentPage.html',context)



def updatehomepage(request):
    context = {'students':Student.objects.all()}
    return render(request,'forms/UpdateHomePage.html',context)


def update(request, pk):
    form = Student.objects.get(id = pk)
    
    if request.method == 'POST':
        Fname = request.POST.get('fname')
        Lname = request.POST.get('lname')
        Phone = request.POST.get('phone')
        Email = request.POST.get('email')
        Level = request.POST.get('Level')
        Gpa = request.POST.get('GPA')
        
        date_string = request.POST.get('date')
        date_format = '%B %d, %Y'
        Dob = datetime.strptime(date_string, date_format).date()

        # Convert Dob to string with a desired format
        Dob_string = Dob.strftime('%Y-%m-%d')  # Format as 'YYYY-MM-DD'
        
        Student.objects.filter(id = pk).update(fname = Fname)
        Student.objects.filter(id = pk).update(lname = Lname)
        Student.objects.filter(id = pk).update(phonenumber = Phone)
        Student.objects.filter(id = pk).update(email = Email)
        Student.objects.filter(id = pk).update(level = Level)
        Student.objects.filter(id = pk).update(gpa = Gpa)
        Student.objects.filter(id = pk).update(dob = Dob_string)
        
        return redirect("/")

    context = {'form':form}
    return render(request,'forms/UpdateInfo.html',context)