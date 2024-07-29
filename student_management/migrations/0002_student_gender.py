# Generated by Django 5.0.6 on 2024-07-01 07:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default=django.utils.timezone.now, max_length=1),
            preserve_default=False,
        ),
    ]