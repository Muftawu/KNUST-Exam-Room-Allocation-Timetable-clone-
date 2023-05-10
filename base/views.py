from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserForm

def home(request):
    if request.user.is_authenticated:
        if request.user.user_type == '2' and request.user.staff_type == 'Student':
            return redirect('student:student_dashboard')
        else:
            return redirect('invigilator:invigilator_dashboard')
    return render(request, 'home.html')


def loginpage(request):   
    if request.user.is_authenticated:
        if request.user.staff_type == 'Invigilator':
            return redirect('invigilator:invigilator_dashboard')
        else:
            return redirect('invigilator:student_dashboard')
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            if request.user.user_type == '2' and request.user.staff_type == 'Invigilator':
                return redirect(reverse('invigilator:invigilator_dashboard'))
            else:
                return redirect('student:student_dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('base:login')
        
    return render(request, 'login.html')

def signup(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse('base:home'))
        else:
            messages.error(request, 'Please cross check your details')
            return redirect('base:signup')
        
    context = {'form': form}
    return render(request, 'signup.html', context)

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(reverse('base:home'))
