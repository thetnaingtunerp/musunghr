# Generated by Django 4.1.7 on 2024-09-17 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_daily_attendance_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_profile',
            name='resign',
            field=models.BooleanField(default=False),
        ),
    ]
