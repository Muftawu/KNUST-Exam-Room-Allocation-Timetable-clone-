from django.urls import path 
from . import views

app_name = 'student'

urlpatterns = [
      path('', views.dashboard, name='student_dashboard'),
      path('view_pdf/', views.view_student_pdf, name='view_student_pdf'),     
]