from django.db import models


class Guardian(models.Model):
    name = models.CharField(max_length=50)
    relation = models.CharField(max_length=50)
    GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'))
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    age = models.IntegerField()
    phone = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class StudentInfo(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField(unique=True)
    std_class = models.IntegerField()
    gender_choice = (('m', 'Male'), ('f', 'Female'))
    gender = models.CharField(max_length=50, choices=gender_choice)
    age = models.IntegerField(blank=True, null=True)
    guard = models.OneToOneField(Guardian, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
    

