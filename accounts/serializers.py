from rest_framework import serializers
from .models import Student, Submission

# write your serializers here
class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'github_url', 'description', 'status', 'submitted_at']
        read_only_fields = ['id', 'status', 'submitted_at']


class StudentRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'email', 'institution', 'registered_at']
        read_only_fields = ['id', 'registered_at']

class StudentProfileSerializer(serializers.ModelSerializer):
    submission = SubmissionSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'full_name', 'email', 'institution', 'registered_at', 'submission']

class TaskSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'github_url', 'description', 'status', 'submitted_at']
        read_only_fields = ['id', 'status', 'submitted_at']