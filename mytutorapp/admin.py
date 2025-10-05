from django.contrib import admin
from .models import Course, Student

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'teacher', 'duration', 'fee', 'schedule']  # ✅ Correct field names

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'course']
from .models import StudyMaterial

admin.site.register(StudyMaterial)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
