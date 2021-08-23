from django.db import models
from utils.models import Fields


class Skill(models.Model):
    LEVELS = (
        (100,'Professional' ),
        (80,'Advanced'),
        (60,'Intermediate'),
        (40, 'Junior'),
        (20, 'Beginner'),
    )
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Fields,on_delete=models.CASCADE)
    proficiency = models.CharField(max_length=19,choices=LEVELS, null=True)
    def __str__(self):
        return self.name