from django.db import models

# Create your models here.

class Trainee (models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER)
    certifications = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __repr__(self):
        return self.first_name + self.last_name

    def full_name(self):
        return self.first_name + ' ' + self.last_name
