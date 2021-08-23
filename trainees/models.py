from django.db import models

from utils.models import Education  
from certifications.models import Certification
from skills.models import Skill

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
    certifications = models.ManyToManyField(Certification)
    education = models.ForeignKey(Education, on_delete=models.CASCADE, blank=True, null=True)
    skills = models.ManyToManyField(Skill)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.first_name + self.last_name

    def full_name(self):
        return self.first_name + ' ' + self.last_name
