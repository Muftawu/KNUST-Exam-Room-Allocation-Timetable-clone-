from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
 
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','index_number', 'first_name', 'last_name', 'programme', 'gender', 'staff_type', 'password1', 'password2')