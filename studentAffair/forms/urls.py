from django.urls import path
from . import views

urlpatterns =[
    path('addStudent',views.addStudent, name='addStudent'),
    path('Departement/<str:pk>',views.DepartmentAssignment, name='Departement'),
    path('updatehomepage',views.updatehomepage, name= 'updatehomepage'),
    path('update/<str:pk>',views.update, name='update'), 
]