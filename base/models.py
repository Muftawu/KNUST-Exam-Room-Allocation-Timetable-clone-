from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.hashers import make_password
from invigilator.utils import generate_uid

PROGRAMMES = (
    ('Civil Engineering', 'Civil Engineering'), 
    ('Computer Engineering', 'Computer Engineering'), 
    ('Aerospace Engineering', 'Aerospace Engineering'), 
    ('Mechanical Engineering', 'Mechanical Engineering'), 
    ('Petroleum Engineering', 'Petroleum Engineering'), 
    ('Electrical Engineering', 'Electrical Engineering'), 
    ('Biomedical Engineering', 'Biomedical Engineering'), 
    ('Petrochemical Engineering', 'Petrochemical Engineering'), 
    ('Materials Engineering', 'Materials Engineering'), 
    ('Chemical Engineering', 'Chemical Engineering'), 
)

class CustomUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            pass 
        username = User.normalize_username(username)
        user = User(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("user_type", 2)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("user_type", 1)

        assert extra_fields["is_staff"]
        assert extra_fields["is_superuser"] 

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    GENDER = (('Male', 'Male'), ('Female', 'Female'))
    user_types = (('1', '1'), ('2', '2'))
    levels = (('100', '100'), ('200', '200'), ('300', '300'), ('400', '400'))
    STAFF_TYPE = (('Student', 'Student'), ('Invigilator', 'Invigilator'))
    
    email = models.EmailField()
    username = models.CharField(max_length=100, null=True, blank=True, unique=True)
    index_number = models.CharField(max_length=10, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    programme = models.CharField(max_length=100, null=True, blank=True, choices=PROGRAMMES)
    level = models.CharField(max_length=10, choices=levels)
    gender = models.CharField(max_length=10, choices=GENDER)
    user_type = models.CharField(max_length=10, choices=user_types, default='2')
    staff_type = models.CharField(max_length=20, blank=True, choices=STAFF_TYPE)
    staff_id = models.CharField(max_length=10, blank=True)

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "index_number"
    REQUIRED_FIELDS = ["username", "email", "gender"]

    def save(self, *args, **kwargs):
        if not self.staff_id:
            dd = generate_uid()
            self.staff_id = dd
            super().save(*args, **kwargs)
    

    def __str__(self):
        if self.user_type == '1':
            return f'{self.username}-{self.index_number}- (Admin)'
        
        if self.user_type == '2' and self.staff_type == 'Student':
            return f'{self.username}-{self.index_number}- (Student)'
        
        if self.user_type == '2' and self.staff_type == 'Invigilator':
            return f'{self.username}-{self.index_number}- (Invigilator)'

    