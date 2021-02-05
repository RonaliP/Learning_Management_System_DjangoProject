from django.contrib import admin
from django.urls import path
from management.views import UpdateStudentDetails, UpdateEducationDetails,Courses,CourseDetails

urlpatterns = [
    path('update-personal-details/', UpdateStudentDetails.as_view(), name='update-details'),
    path('update-education-details/', UpdateEducationDetails.as_view(), name='update-edu-details'),
    path('courses/', Courses.as_view(), name='courses'),
    path('course/<int:id>', CourseDetails.as_view(), name='course'),
]