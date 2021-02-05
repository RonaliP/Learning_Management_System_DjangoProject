from authentication.models import User
from management.models import Student, EducationDetails, Mentor
from django.dispatch import receiver
from django.db.models.signals import post_save
from authentication.utils import EmailMessage


@receiver(post_save, sender=User)
def create_student_details(sender, instance, created, **kwargs):
    """ receiver function that will create profile for an user instance
        Args:
            sender ([model class]): [user model class]
            instance ([model object]): [user model instance that is actually being saved]
            created ([boolean]): [true if new record has created in user model]
    """
    if created:
        if instance.role == 'Student':
            student = Student.objects.create(student=instance)
            EducationDetails.objects.create(student=student)
        else:
            Mentor.objects.create(mentor=instance)