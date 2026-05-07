from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.generics import GenericAPIView
from rest_framework.generics import CreateAPIView, ListAPIView


from .models import Student
from .serializers import (StudentRegistrationSerializer, StudentProfileSerializer, TaskSubmissionSerializer,)

# Create your views here.
def index(request): 
    return render(request, 'index.html')

class RegisterStudentView(CreateAPIView):
    """
    POST /api/students/register/
    Register a new student.
    """
    serializer_class = StudentRegistrationSerializer    
    queryset = Student.objects.all()
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED,)

class SubmitTaskView(CreateAPIView):
    """
    POST /api/students/<student_id>/submit/
    Submit a task (GitHub URL) for a registered student.
    A student can only have one submission.
    """

    serializer_class = TaskSubmissionSerializer
    queryset = Student.objects.all()
    
    def post(self, request, student_id):
        try:
            student = Student.objects.get(pk=student_id)
        except Student.DoesNotExist:
            return Response(
                {'detail': 'Student not found.'},
                status=status.HTTP_404_NOT_FOUND,)

        if hasattr(student, 'submission'):
            return Response(
                {'detail': 'A submission already exists for this student.'},
                status=status.HTTP_400_BAD_REQUEST,)

        serializer = TaskSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(student=student)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentProfileView(ListAPIView):
    """
    GET /api/students/<student_id>/profile/
    Retrieve a student's profile along with their submission status.
    """

    def get(self, request, student_id):
        try:
            student = Student.objects.select_related('submission').get(pk=student_id)
        except Student.DoesNotExist:
            return Response(
                {'detail': 'Student not found.'},
                status=status.HTTP_404_NOT_FOUND,)

        serializer = StudentProfileSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)