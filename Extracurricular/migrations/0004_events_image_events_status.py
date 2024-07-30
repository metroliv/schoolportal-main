# Generated by Django 5.0.7 on 2024-07-30 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Extracurricular', '0003_events_date_events_description_events_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='event_images/'),
        ),
        migrations.AddField(
            model_name='events',
            name='status',
            field=models.CharField(choices=[('upcoming', 'Upcoming'), ('ongoing', 'Ongoing'), ('completed', 'Completed')], default='upcoming', max_length=10),
        ),
    ]