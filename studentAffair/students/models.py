from django.db import models 

class Student(models.Model):

    fname = models.CharField(max_length = 50, default='First name', verbose_name='First Name')
    lname = models.CharField(max_length = 50, default='Last name', verbose_name='Last Name')
    id = models.CharField(max_length=8,primary_key=True, default='20210000', verbose_name='ID')
    level = models.CharField(max_length = 1, default='1')
    gpa = models.DecimalField(max_digits = 3, decimal_places=2, default='4.00', verbose_name='GPA')
    gender = models.CharField(max_length = 6, choices=[('Male','Male'),('Female','Female')])
    dob = models.DateField(default='2023-05-24', verbose_name='Date Of Birth')
    email = models.CharField(max_length=50, default="NULL", verbose_name = 'Email')
    phonenumber = models.CharField(max_length = 11, default= '01000000000', verbose_name='Phone Number')
    status = models.CharField(max_length = 8,choices = [('Active','Active'),('InActive','InActive')])
    departement = models.CharField(max_length=4,default='NULL', choices=[('NULL','NULL'),('CS','CS'),('AI','AI'),('IS','IS'),('IT','IT'),('DS','DS')])

    def __str__(self):
        return self.fname
    