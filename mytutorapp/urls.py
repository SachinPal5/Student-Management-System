from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.course_list, name='courses'),
    path('register/', views.register, name='register'),
    path('study-material/', views.study_material, name='study_material'),
    path('login/', views.student_login, name='login'),
    path('logout/', views.student_logout, name='logout'),
    path('send-reminders/', views.send_fee_reminders, name='send_fee_reminders'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('fee-management/', views.fee_management, name='fee_management'),
    path('add-payment/<int:student_id>/', views.add_payment, name='add_payment'),

    path('dashboard/', views.dashboard, name='dashboard'),
]
