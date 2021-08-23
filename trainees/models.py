from django.db import models

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

class Education(models.Model):
    # student = models.ForeignKey(Trainee, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    institution = models.ForeignKey(Establishment, on_delete=models.CASCADE)
    major = models.CharField(max_length=120)
    completion = models.DateField()

    def __str__(self):
        return self.title


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
