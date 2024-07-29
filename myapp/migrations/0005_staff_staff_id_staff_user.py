# Generated by Django 5.0.6 on 2024-07-14 14:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_usersettings'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='staff_id',
            field=models.CharField(default='STAFF_DEFAULT', max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='user',
            field=models.OneToOneField(default=100, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]