from django.urls import path
from . import views


urlpatterns = [
    path('studentCheck/<int:pk_id>/', views.studentCheck,name='studentCheck'),
    path('delStudent/<int:pk_id>/', views.delStudent, name='delStudent'),
    path('statueStudent/<int:pk_id>/', views.statueStudent, name='statueStudent')
]