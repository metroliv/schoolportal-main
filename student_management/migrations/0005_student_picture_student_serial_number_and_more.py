# Generated by Django 5.0.6 on 2024-07-13 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0004_student_admission_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='student_pictures/'),
        ),
        migrations.AddField(
            model_name='student',
            name='serial_number',
            field=models.CharField(blank=True, max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='admission_number',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]
