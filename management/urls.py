from django.contrib import admin
from django.urls import path
from management.views import UpdateStudentDetails, UpdateEducationDetails

urlpatterns = [
    path('update-details/', UpdateStudentDetails.as_view(), name='update-details'),
    path('update-edu-details/', UpdateEducationDetails.as_view(), name='update-edu-details'),
]