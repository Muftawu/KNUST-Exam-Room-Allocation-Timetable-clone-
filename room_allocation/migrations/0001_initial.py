# Generated by Django 4.2 on 2023-05-08 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_type', models.CharField(blank=True, choices=[('Midsem', 'Midsem'), ('End of Sem', 'End of Sem')], default='Midsem', max_length=200, null=True)),
                ('semester', models.CharField(blank=True, choices=[('First', 'First'), ('Second', 'Second')], default='First', max_length=100, null=True)),
                ('academic_year', models.CharField(blank=True, choices=[('2020/2021', '2020/2021'), ('2021/2022', '2021/2022'), ('2022/2023', '2022/2023'), ('2023/2024', '2023/2024')], default='2021/2022', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_name', models.CharField(blank=True, max_length=100, null=True)),
                ('paper_code', models.CharField(blank=True, max_length=100, null=True)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('room', models.CharField(blank=True, max_length=100, null=True)),
                ('building', models.CharField(blank=True, max_length=100, null=True)),
                ('floor', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Qrcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('code', models.UUIDField()),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programme', models.CharField(blank=True, max_length=100, null=True)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room_allocation.exam')),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room_allocation.paper')),
                ('qcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room_allocation.qrcode')),
            ],
        ),
    ]
