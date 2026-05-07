from django.db import models

# Create your models here.

class Student(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    institution = models.CharField(max_length=255)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}- ({self.email})"


class Submission(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('verified', 'Verified'),
        ('rejected', 'Rejected'),
    ]

    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='submission',)
    github_url = models.URLField()
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission by {self.student.full_name} [{self.status}]"