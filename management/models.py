from django.db import models
from authentication.models import User

class Course(models.Model):
    course_name = models.CharField(blank=False, unique=True, db_index=True, max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Mentor(models.Model):
    mentor = models.OneToOneField(to=User, on_delete=models.CASCADE)
    course = models.ManyToManyField(to=Course, related_name='mentor_course')
    createdAt = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Student(models.Model):
    student = models.OneToOneField(to=User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=10)
    alternate_contact = models.CharField(max_length=10)
    relation_with_alternate_contact = models.CharField(blank=False, max_length=50)
    current_location = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    git_link = models.CharField(max_length=50)
    yr_of_exp = models.FloatField(default=0)
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True)

class EducationDetails(models.Model):
    student = models.OneToOneField(to=Student, on_delete=models.CASCADE)
    course = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)
    percentage = models.FloatField(default=0.0)
    joined_at = models.DateField(auto_now_add=True)
    till = models.DateField(auto_now=True)

class Performance(models.Model):
    student = models.OneToOneField(to=Student, on_delete=models.CASCADE)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    mentor = models.ForeignKey(to=Mentor, on_delete=models.CASCADE)
    current_score = models.FloatField(blank=False)
    updated_at = models.DateField(auto_now=True)


class MentorStudent(models.Model):
    student = models.OneToOneField(to=User, on_delete=models.CASCADE)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    mentor = models.ForeignKey(to=Mentor, on_delete=models.CASCADE)