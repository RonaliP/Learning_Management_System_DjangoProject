from django.test import TestCase
from authentication.models import User
from management.models import Student, EducationDetails, Mentor
from management.serializers import MentorsSerializer

class UserTest(TestCase):

    def setUp(self):
        self.admin = User.objects.create(username='admin',
                                         first_name='Rona',
                                         last_name='Panigrahy',
                                         email='Ronali@gmail.com',
                                         password='67678989',
                                         role='Admin')
        self.student = User.objects.create(username='student',
                                           first_name='Sona',
                                           last_name='Panigrahy',
                                           email='student@gmail.com',
                                           password='898989',
                                           role='Student')

        self.mentor = User.objects.create(username='mentor',
                                          first_name='sahil',
                                          last_name='raj',
                                          email='mentor@gmail.com',
                                          password='0000',
                                          role='Mentor')


    def test_create_user(self):
        user = User.objects.get(username='student')
        self.assertEqual(user.get_full_name(), 'Sona Panigrahy')

    def test_create_student_details(self):
        student_details = Student.objects.get(student=self.student)
        self.assertEqual(student_details.contact, "")

    def test_create_mentor(self):
        mentor = Mentor.objects.get(mentor=self.mentor)
        serializer = MentorsSerializer(mentor.course.all(), many=True)
        self.assertEqual(serializer.data, [])

    def test_create_education_details(self):
        student_details = Student.objects.get(student=self.student)
        education_details = EducationDetails.objects.get(student=student_details)
        self.assertEqual(education_details.institution, "")
