from django.urls import path
from .views import RegisterStudentView, SubmitTaskView, StudentProfileView

# write your urls here

urlpatterns = [
    path('students/register/', RegisterStudentView.as_view(), name='student-register'),
    path('students/<int:student_id>/submit/', SubmitTaskView.as_view(), name='task-submit'),
    path('students/<int:student_id>/profile/', StudentProfileView.as_view(), name='student-profile'),
]