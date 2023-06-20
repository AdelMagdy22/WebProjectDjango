from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from students.models import Student 
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

@api_view()
def studentCheck(request, pk_id):
    try:
        student = Student.objects.get(id=pk_id)
        return Response(status= status.HTTP_204_NO_CONTENT)
    except:
        return Response(status= status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['DELETE'])
def delStudent(request, pk_id):
    student = Student.objects.get(pk=pk_id)
    student.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['POST'])
def statueStudent(request, pk_id):
    student = Student.objects.get(pk=pk_id)
    if student.status == 'Active':
        Student.objects.filter(id = pk_id).update(status = "InActive")
    else:
        Student.objects.filter(id = pk_id).update(status = "Active")
    
    return Response(status=status.HTTP_204_NO_CONTENT)
