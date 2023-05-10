from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from base.models import User

@login_required(login_url='invigilator:invigilator_login')
def dashboard(request):
    return render(request, 'invigilator_dashboard.html')


