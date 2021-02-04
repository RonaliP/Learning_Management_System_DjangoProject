from django.contrib import admin
from management.models import Course, Mentor, Student, MentorStudent, Performance, EducationDetails

admin.site.register(Course)
admin.site.register(MentorStudent)
admin.site.register(Mentor)
admin.site.register(Student)
admin.site.register(EducationDetails)
admin.site.register(Performance)