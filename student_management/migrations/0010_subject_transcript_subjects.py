# Generated by Django 5.0.6 on 2024-07-14 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0009_remove_transcript_content_transcript_total_marks_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='transcript',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='student_management.subject'),
        ),
    ]