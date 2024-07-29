from django.db import models
import uuid


class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    location = models.CharField(max_length=100)
    hobby = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    admission_number = models.CharField(max_length=12, unique=True, blank=True)
    serial_number = models.CharField(max_length=8, unique=True, editable=False)
    picture = models.ImageField(upload_to='student_pictures/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.admission_number:
            self.admission_number = self.generate_admission_number()
        if not self.serial_number:
            self.serial_number = self.generate_serial_number()
        super(Student, self).save(*args, **kwargs)

    def generate_admission_number(self):
        return str(uuid.uuid4().int)[:12]

    def generate_serial_number(self):
        return str(uuid.uuid4().int)[:8]

    def __str__(self):
        return self.name

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='marks')
    subject = models.CharField(max_length=100)
    marks_obtained = models.FloatField()

    def __str__(self):
        return f"{self.student.name} - {self.subject}"

class Transcript(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    total_marks = models.FloatField(default=0)

    def __str__(self):
        return f"Transcript for {self.student.name}"
