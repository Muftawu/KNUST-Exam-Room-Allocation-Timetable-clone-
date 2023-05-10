from django.db import models

import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

EXAM_TYPE = (
    ('Mid-Semester', 'Mid-Semester'),
    ('End of Semester', 'End of Semester'),
)

SEMESTER_TYPE = (('First', 'First'), ('Second', 'Second'))

ACADEMIC_YEAR = (
    ('2020/2021', '2020/2021'),
    ('2021/2022', '2021/2022'),
    ('2022/2023', '2022/2023'),
    ('2023/2024', '2023/2024')
)

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
)

class Exam(models.Model):
    exam_type = models.CharField(max_length=200, choices=EXAM_TYPE, default='Mid-Semester', null=True, blank=True)
    semester = models.CharField(max_length=100, choices=SEMESTER_TYPE, default='First', null=True, blank=True)
    academic_year = models.CharField(max_length=100, choices=ACADEMIC_YEAR, default='2021/2022', null=True, blank=True)

    def __str__(self):
        return f'{self.exam_type} - {self.semester} semester - {self.academic_year}'

class Paper(models.Model):
    paper_name = models.CharField(max_length=100, null=True, blank=True)
    paper_code = models.CharField(max_length=100, null=True, blank=True)
    time = models.TimeField()
    date = models.DateField()
    room = models.CharField(max_length=100, null=True, blank=True)
    building = models.CharField(max_length=100, null=True, blank=True)
    floor = models.CharField(max_length=100, null=True, blank=True)
    college = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.paper_code}-{self.paper_name}-{self.room}'

class Qrcode(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    paper = models.ForeignKey(Paper, on_delete=models.SET_NULL, null=True, blank=True)
    code_img = models.ImageField(upload_to='qrcode_images', null=True, blank=True)

    def __str__(self):
        return f'{self.paper.paper_code}-{self.paper.room}'
    
    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.paper.room)
        canvas = Image.new('RGB',(290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        
        fname = f'qr_code-{self.paper.paper_code}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.code_img.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)
    
class Timetable(models.Model):
    programme = models.CharField(max_length=100, null=True, blank=True, choices=PROGRAMMES)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    qcode = models.ForeignKey(Qrcode, on_delete=models.CASCADE)

    @property
    def imageURL_pdf(self):
        try:
            url = self.qcode.code_img.path
        except:
            url = ''
        return url 
    
    @property
    def imageURL(self):
        try:
            url = self.qcode.code_img.url
        except:
            url = ''
        return url 
    
    def __str__(self):
        return f'{self.programme}-{self.paper.paper_name}'
