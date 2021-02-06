from rest_framework import serializers
from management.models import Student, EducationDetails,Course,Mentor,MentorStudent,Performance


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

class MentorsSerializer(serializers.ModelSerializer):
    mentor = serializers.StringRelatedField(read_only=True)
    course = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Mentor
        fields = ['mentor','course']


class MentorCourseMappingSerializer(serializers.ModelSerializer):
    mentor = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Mentor
        fields = ['mentor', 'course']


class MentorStudentMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorStudent
        fields = ['student', 'course', 'mentor']


class MentorStudentUpdateMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorStudent
        fields = ['student', 'course', 'mentor']
        extra_kwargs = {'student': {'read_only': True}}


class MentorStudentListSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField(read_only=True)
    course = serializers.StringRelatedField(read_only=True)
    mentor = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = MentorStudent
        fields = ['student', 'course', 'mentor']


class PerformanceSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField(read_only=True)
    mentor = serializers.StringRelatedField(read_only=True)
    course = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Performance
        fields = '__all__'

