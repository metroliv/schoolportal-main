# Generated by Django 5.0.6 on 2024-07-13 17:15

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0006_alter_student_admission_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='serial_number',
            field=models.CharField(default=uuid.uuid4, max_length=100, unique=True),
        ),
    ]
