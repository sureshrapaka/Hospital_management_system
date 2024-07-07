from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin = models.BooleanField('Is Admin',default=False)
    is_doctor = models.BooleanField('Is Doctor',default=False)
    is_receptionist = models.BooleanField('Is Receptionist',default=False)
    is_labtechnician = models.BooleanField('Is Labtechnician',default=False)
    is_accountant = models.BooleanField('Is Accountant',default=False)
    is_employee = models.BooleanField('Is Employee',default=False)