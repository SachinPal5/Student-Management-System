from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
import requests
from collections import defaultdict

from .models import Student, StudyMaterial, Course, FeePayment
from .forms import StudentForm


def home(request):
    return render(request, 'home.html')

def send_sms(phone, message):
    print(f"SMS to {phone}: {message}")
    # Use an SMS API like Fast2SMS here

def send_whatsapp(phone, message):
    print(f"WhatsApp to {phone}: {message}")
    # Use WhatsApp Cloud API or Gupshup API here
@staff_member_required
def send_fee_reminders(request):
    from .models import Student
    if request.method == 'POST':
        students_with_due = Student.objects.filter(fee_due__gt=0)
        for student in students_with_due:
            message = f"Dear {student.name}, your tuition fee of ₹{student.fee_due} is pending. Please pay soon. - Khushi Group Tuition"
            send_sms(student.phone, message)
            send_whatsapp(student.phone, message)
        messages.success(request, "✅ Reminders sent successfully.")
        return redirect('send_fee_reminders')
    return render(request, 'send_reminders.html')


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})


@staff_member_required
def admin_dashboard(request):
    students = Student.objects.select_related('course').all().order_by('-fee_due')
    return render(request, 'admin_dashboard.html', {'students': students})

def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            course = form.cleaned_data['course']
            password = form.cleaned_data['password']

            # ✅ Check for duplicate
            if User.objects.filter(username=email).exists():
                messages.error(request, "❌ This email is already registered.")
                return redirect('register')

            # ✅ Create user and student
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = name
            user.save()

            student = Student(user=user, name=name, email=email, phone=phone, course=course)
            student.save()

            messages.success(request, "✅ Registered successfully. Please login.")
            return redirect('login')
    else:
        form = StudentForm()

    return render(request, 'register.html', {'form': form})


   


def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


def student_logout(request):
    logout(request)
    return redirect('home')


@login_required
def dashboard(request):
    try:
        student = Student.objects.get(user=request.user)
        materials = StudyMaterial.objects.filter(course=student.course).order_by('title')

        return render(request, 'dashboard.html', {
            'student': student,
            'materials': materials
        })
    except Student.DoesNotExist:
        return render(request, 'dashboard.html', {
            'student': None,
            'materials': [],
            'error': "No student profile found for this user. Please contact admin."
        })


from collections import defaultdict
from .models import StudyMaterial

def study_material(request):
    materials = StudyMaterial.objects.select_related('course').all().order_by('course__title', 'title')
    grouped = defaultdict(list)

    for material in materials:
        if material.course:  # ✅ prevents 'NoneType' error
            grouped[material.course.title].append(material)

    return render(request, 'study_material.html', {'grouped_materials': grouped})
@staff_member_required
def fee_management(request):
    students = Student.objects.all().order_by('name')
    return render(request, 'fee_management.html', {'students': students})


from decimal import Decimal  # 👈 Import this at the top

@staff_member_required
def add_payment(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        amount = Decimal(request.POST['amount'])  # 👈 Use Decimal
        note = request.POST.get('note', '')

        FeePayment.objects.create(student=student, amount=amount, note=note)
        student.fee_due -= amount
        student.save()

        messages.success(request, f"✅ ₹{amount} payment recorded for {student.name}.")
        return redirect('fee_management')

    return render(request, 'add_payment.html', {'student': student})

from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_staff or user.is_superuser  # or use custom `is_teacher` if available

@user_passes_test(is_admin)
def admin_dashboard(request):
    students = Student.objects.select_related('course').all().order_by('-fee_due')
    return render(request, 'admin_dashboard.html', {'students': students})

@login_required
def dashboard(request):
    if request.user.is_staff:
        return redirect('admin_dashboard')  # Prevent staff from using student dashboard

    try:
        student = Student.objects.get(user=request.user)
        materials = StudyMaterial.objects.filter(course=student.course).order_by('title')
        return render(request, 'dashboard.html', {
            'student': student,
            'materials': materials
        })
    except Student.DoesNotExist:
        return redirect('home')  # Or show an error
    