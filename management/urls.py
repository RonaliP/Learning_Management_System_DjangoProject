from django.contrib import admin
from django.urls import path
from management.views import UpdateStudentDetails, UpdateEducationDetails,Courses,CourseDetails,Mentors,Mentordetails,MentorCourseMapping,MentorStudentMapping, MentorStudentDetails, PerformanceAPI, PerformanceDetailsAPI



urlpatterns = [
    path('update-personal-details/<int:id>', UpdateStudentDetails.as_view(), name='update-details'),
    path('update-education-details/<int:id>', UpdateEducationDetails.as_view(), name='update-edu-details'),
    path('courses/', Courses.as_view(), name='courses'),
    path('course/<int:id>', CourseDetails.as_view(), name='course'),
    path('mentors/', Mentors.as_view(), name='mentors'),
    path('mentor/<int:mentor_id>', Mentordetails.as_view(), name='mentor'),
    path('mentor/<int:id>', Mentordetails.as_view(), name='mentor'),
    path('mentor-course/<int:mentor_id>', MentorCourseMapping.as_view(), name='mentor-course'),
    path('mentor-student/', MentorStudentMapping.as_view(), name='mentor-student'),
    path('mentor-student/<int:search_id>', MentorStudentDetails.as_view(), name='mentor-student-details'),
    path('performance/', PerformanceAPI.as_view(), name='performance'),
    path('performance/<int:id>', PerformanceDetailsAPI.as_view(), name='performance-details')

]