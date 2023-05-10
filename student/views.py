from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from base.models import User
from room_allocation.models import Paper, Timetable, Exam, Qrcode

from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template.loader import get_template

courses = ['Computer Engineering','Materials Engineering',]

@login_required(login_url='studentLogin')
def dashboard(request):
    try:
        for i in range(len(courses)):
            if request.user.staff_type == 'Student' and request.user.programme == courses[i]:
                timetable = Timetable.objects.filter(programme=courses[i])
                exam_type = Timetable.objects.filter(programme=courses[i])[0].exam.exam_type
                academic_year = Timetable.objects.filter(programme=courses[i])[0].exam.academic_year
    except:
        exam_type = 'default midsem'
        academic_year = '2023'

    context = {'timetable': timetable, 'exam_type': exam_type, 'academic_year': academic_year}
    return render(request, 'student_dashboard.html', context)


@login_required(login_url='studentLogin')
def view_student_pdf(request):
    template_path = 'student_pdf.html'
    fname, lname = request.user.first_name, request.user.last_name
    index_number = request.user.index_number
    print(fname, lname, index_number)

    try:
        for i in range(len(courses)):
            if request.user.staff_type == 'Student' and request.user.programme == courses[i]:
                timetable = Timetable.objects.filter(programme=courses[i])
                exam_type = Timetable.objects.filter(programme=courses[i])[0].exam.exam_type
                academic_year = Timetable.objects.filter(programme=courses[i])[0].exam.academic_year
    except:
        exam_type = 'default midsem'
        academic_year = '2023'

    context = {'timetable': timetable, 'fname': fname, 'lname': lname, 'index_number': index_number}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def studentLogin(request):
    if request.user.is_authenticated:
        return redirect('student:student_dashboard')
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            print(user)
            login(request, user)
            if request.user.user_type and request.user:
                return redirect('invigilator:invigilator_dashboard')
            else:
                return redirect('student:student_dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('student:studentLogin')
    return render(request, 'student_login.html')

