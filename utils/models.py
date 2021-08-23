from django.db import models
# from trainees.models import Trainee

# Create your models here.
TYPES = (
    ("S", "School"),
    ("C", "Company")
)

class Fields(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Establishment(models.Model):

    name = models.CharField(max_length=250)
    type = models.CharField(max_length=1, choices=TYPES)

    def __str__(self):
        return self.name

class Experience(models.Model):
    ROLES = (
        ('S', 'Senior Developer'),
        ('J', 'Junior Developer'),
        ('A', 'Apprentice Developer'),
        ('O', 'Other'),
    )
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE)
    role = models.CharField(max_length=1,choices=ROLES)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return self.role

class Education(models.Model):
    # student = models.ForeignKey(Trainee, on_delete=models.CASCADE)
    institution = models.ForeignKey(Establishment, on_delete=models.CASCADE)
    major = models.CharField(max_length=120)
    completion = models.DateField()

    def __str__(self):
        return self.major