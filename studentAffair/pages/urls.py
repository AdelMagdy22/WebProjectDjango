from django.urls import path
from . import views

urlpatterns = [
    path('',views.home ,name='Home'),
    # path('addStudent',views.addStudent, name='addStudent'),
    # path('delete',views.delete, name='delete'),
    # path('Departmnet',views.DepartmentAssignment, name='Departmnet'),
    path('login',views.login, name='login'),
    path('tutorial',views.tutorial, name= 'tutorial'),
    #path('search',views.search, name= 'search'),
    # path('updatehomepage',views.updatehomepage, name= 'updatehomepage'),
    # path('addStudent',views.addStudent, name= 'addStudent'),
    #path('view',views.view, name = 'view'),
]