# Generated by Django 5.0.6 on 2024-07-15 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_staff_staff_id_staff_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subscribed_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
