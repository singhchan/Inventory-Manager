from django.db import models
from django.db.models.deletion import SET_NULL
from django.core.validators import (EmailValidator, MaxValueValidator, MinValueValidator)
from django.db.models.fields import CharField
from django.db.models.fields.related import ManyToManyField, OneToOneField


# Create your models here.
# class Employee(models.Model):
#     GENDER = (
#         ('f', 'Female'),
#         ('m', 'Male'),
#         ('n', 'NonBinary'),
#         ('u', 'Undisclosed')
#     )
#     DEPARTMENT = (
#         ('IT', 'Information Technology'),
#         ('FN', 'Finance'),
#         ('HR', 'Human Resources')
#     )
#     id = OneToOneField('auth.User', on_delete=models.CASCADE, primary_key=True)
#     name = CharField(max_length=100)
#     department = CharField(max_length=2, choices=DEPARTMENT)
#     gender = CharField(max_length=1, choices=GENDER)
#     assets = ManyToManyField('Assets')

#     def __str__(self):
#         return self.name

class Employee(models.Model):
    GENDER = (
        ('f', 'Female'),
        ('m', 'Male'),
        ('n', 'NonBinary'),
        ('u', 'Undisclosed')
    )
    DEPARTMENT = (
        ('IT', 'Information Technology'),
        ('FN', 'Finance'),
        ('HR', 'Human Resources')
    )
    id = models.OneToOneField(
        'auth.User',
        on_delete=models.CASCADE,
        primary_key=True
    )
    name = models.CharField(max_length = 100)
    age = models.IntegerField(
        null=True, 
        validators=[MinValueValidator(16, 'Employee too young!'), MaxValueValidator(75, 'Employee too old!')]
    )
    department = models.CharField(max_length = 100, choices=DEPARTMENT, null=True, blank=True)
    phonenumber = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length = 100, unique=True, null=True, blank=True, validators = [EmailValidator("Invalid Email ID!")])
    gender = models.CharField(max_length=1, choices=GENDER, null=True)
    image = models.ImageField(default = 'Images/avatar.png', upload_to='Images')
    assets = models.ManyToManyField('Assets', through = 'Possesion')
    def __str__(self):
        return self.name

class Assets(models.Model):
    id = models.CharField(max_length = 10, unique=True, primary_key=True)
    name = models.CharField(max_length = 100)
    totalstock = models.IntegerField(null=True, blank=True)
    onhand = models.IntegerField(null=True, blank=True)
    minimumrequired = models.IntegerField(null=True, blank = True)
    faulty = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Possesion(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.RESTRICT)
    product = models.ForeignKey('Assets', on_delete=models.RESTRICT)
    class Meta:
        unique_together = (("employee", "product"),)
    fromdate = models.DateTimeField(blank=True)
    issueraised = models.BooleanField(default=False)
    underprocess = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.employee) + ' ' + str(self.product)