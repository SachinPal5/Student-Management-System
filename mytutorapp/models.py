from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    fee = models.DecimalField(max_digits=8, decimal_places=2)
    schedule = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    fee_due = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    admission_date = models.DateField(auto_now_add=True) 
    is_teacher = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class StudyMaterial(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to='materials/', null=False, blank=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    video_link = models.URLField(blank=True, null=True)

    def __str__(self):
        course_title = self.course.title if self.course else "No Course"
        return f"{self.title} ({course_title})"
class FeePayment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)  # 🗓️ Automatically today's date
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student.name} - ₹{self.amount} on {self.payment_date}"
