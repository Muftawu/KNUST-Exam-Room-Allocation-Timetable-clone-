from django.urls import path 
from . import views

app_name = 'invigilator'

urlpatterns = [
      path('invigilator_dashboard', views.dashboard, name='invigilator_dashboard'), 
]