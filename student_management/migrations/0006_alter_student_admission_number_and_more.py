# Generated by Django 5.0.6 on 2024-07-13 17:09

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0005_student_picture_student_serial_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admission_number',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='serial_number',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
