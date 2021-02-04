from authentication.models import User
from management.models import Student, EducationDetails
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=User)
def create_student_details(sender, instance, created, **kwargs):

    if created and instance.role == 'Student':
        Student.objects.create(student=instance)
        EducationDetails.objects.create(student=instance)