# Generated by Django 4.1.7 on 2024-09-25 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_daily_attendance_report_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily_attendance_report',
            name='weekno',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
