from django.db import models

class Employee(models.Model):
    DESIGNATION_CHOICES = [
        ('HR', 'HR'),
        ('Manager', 'Manager'),
        ('Sales', 'Sales'),
    ]

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    COURSES_CHOICES = [
        ('MCA', 'MCA'),
        ('BCA', 'BCA'),
        ('BSC', 'BSC'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)
    designation = models.CharField(max_length=50, choices=DESIGNATION_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    courses = models.CharField(max_length=200,choices=COURSES_CHOICES)  # Store selected courses as a comma-separated string
    img_upload = models.ImageField(upload_to='uploads/', blank=True, null=True)  # This should be 'img_upload'

    def __str__(self):
        return self.name


