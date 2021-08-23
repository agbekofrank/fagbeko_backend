from django.db import models

from utils.models import Establishment

# Create your models here.
class Certification(models.Model):
    LEVELS = (
        ('P','Professional'),
        ('PG', 'Post Graduate'),
        ('D', 'Degree'),
        ('DP', 'Diploma'),
        ('U', 'Under Graduate'),
        ('O', 'Other')

    )
    skills_level = models.CharField(max_length=120, choices=LEVELS)
    awarded_by = models.ManyToManyField(Establishment)
    type = models.CharField(max_length=120, choices=LEVELS)
    completion = models.DateField()