# Generated by Django 4.2 on 2023-05-08 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_allocation', '0003_alter_qrcode_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='college',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
