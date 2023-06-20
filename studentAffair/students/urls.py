from django.urls import path
from . import views


urlpatterns = [
    path('search',views.search, name= 'search'),
    path('view',views.view, name = 'view'),
    path('delete',views.delete, name ='delete'),
]