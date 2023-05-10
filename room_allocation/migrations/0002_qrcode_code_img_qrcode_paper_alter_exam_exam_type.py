# Generated by Django 4.2 on 2023-05-08 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room_allocation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode',
            name='code_img',
            field=models.ImageField(blank=True, null=True, upload_to='qrcode_images'),
        ),
        migrations.AddField(
            model_name='qrcode',
            name='paper',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='room_allocation.paper'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='exam_type',
            field=models.CharField(blank=True, choices=[('Mid-Semester', 'Mid-Semester'), ('End of Semester', 'End of Semester')], default='Mid-Semester', max_length=200, null=True),
        ),
    ]