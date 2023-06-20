from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pages.urls')),
    path('students/', include('students.urls')),
    path('studentAPI/', include('studentAPI.urls')),
    path('forms/',include('forms.urls')),
]
