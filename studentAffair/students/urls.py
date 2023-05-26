from django.urls import path
from . import views


urlpatterns = [
    path('search',views.search, name= 'search'),
    path('view',views.view, name = 'view'),
    path('delete',views.delete, name ='delete'),
    path('deleteConfirm/<str:pk>', views.deleteConfirm, name='deleteConfirm'),
    path('viewConfirm/<str:pk>', views.viewConfirm, name='viewConfirm'),
]