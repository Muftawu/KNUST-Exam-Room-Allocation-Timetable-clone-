# Generated by Django 4.2 on 2023-05-08 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_allocation', '0002_qrcode_code_img_qrcode_paper_alter_exam_exam_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]