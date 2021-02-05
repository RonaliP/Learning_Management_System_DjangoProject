from django.shortcuts import render, redirect
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from management.serializers import UpdateStudentDetailsSerializer, UpdateEducationDetailsSerializer,AddCourseSerializer
from management.models import Student, EducationDetails,Course
from authentication.permissions import IsAdmin


class UpdateStudentDetails(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateStudentDetailsSerializer

    def get_object(self):
        """
            Returns current logged in student profile instance
        """
        return self.request.user.student

    def get_education_details(self):
        return EducationDetails.object.get(student=self.get_object())

    def performe_update(self, serializer):
        """
            Save the updated user student instance
        """
        student = serializer.save(student=self.request.user)
        return Response({'response': student}, status=status.HTTP_200_OK)


class UpdateEducationDetails(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateEducationDetailsSerializer

    def get_object(self):
        return EducationDetails.objects.get(student=self.request.user.student)

    def performe_update(self, serializer):
        """
            Save the updated user student instance
        """
        student = serializer.save(student=self.request.user)
        return Response({'response': student}, status=status.HTTP_200_OK)


class Courses(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsAdmin)
    serializer_class = AddCourseSerializer

    def get_queryset(self):
        """
            Returns a list of all create courses
        """
        return Course.objects.all()

    def perform_create(self, serializer):
        """
            create a new course instance
        """
        course = serializer.save()
        return Response({'response': course}, status=status.HTTP_201_CREATED)


class CourseDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsAdmin)
    serializer_class = AddCourseSerializer
    queryset = Course.objects.all()
    lookup_field = "id"

    def perform_update(self, serializer):
        course = serializer.save()
        return Response({'response': course}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()
        return Response({'response': 'Course is deleted permanently.'}, status=status.HTTP_204_NO_CONTENT)
