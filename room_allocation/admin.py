from django.contrib import admin
from . models import Exam, Qrcode, Paper, Timetable

admin.site.register(Exam)
admin.site.register(Qrcode)
admin.site.register(Paper)
admin.site.register(Timetable)
