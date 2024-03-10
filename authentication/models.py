from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

USERTYPE = [("Employee", "EMPLOYEE"), ("Employer", "EMPLOYER")]


class UserModel(AbstractUser):

    userType = models.CharField(max_length=10, choices=USERTYPE, default="EMPLOYEE")
