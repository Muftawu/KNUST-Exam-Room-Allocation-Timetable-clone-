from django.contrib import admin
from .models import User

admin.site.site_header = "Personal Timetable"

admin.site.register(User)