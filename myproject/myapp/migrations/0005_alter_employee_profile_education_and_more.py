# Generated by Django 5.0.2 on 2024-02-20 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_township_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_profile',
            name='education',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='employee_profile',
            name='employee_name',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='employee_profile',
            name='finger_id',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='employee_profile',
            name='phone',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='employee_profile',
            name='race',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='employee_profile',
            name='religion',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='employee_profile',
            name='ssb_id',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]