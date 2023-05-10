from django.urls import path 
from . import views

app_name = 'base'

urlpatterns = [
      path('', views.home, name='home'),
      path('login/', views.loginpage, name='login'),
      path('signup/', views.signup, name='signup'),
      path('logout/', views.logoutpage, name='logout'),
]