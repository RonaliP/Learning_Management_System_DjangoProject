from rest_framework import serializers
from management.models import Student, EducationDetails,Course


class UpdateStudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['contact', 'alternate_contact', 'relation_with_alternate_contact','current_location','Address','git_link','yr_of_exp']

class UpdateEducationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationDetails
        fields = ['course', 'institution', 'percentage']

class AddCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name']