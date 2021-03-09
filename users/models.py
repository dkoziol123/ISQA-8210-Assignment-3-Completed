from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    department = models.CharField(max_length=50, default=' ', null=True, blank=True)
    employee_cell_phone = models.CharField (max_length=50, default=' ', null=True, blank=True)


#class Image(models.Model):
    #image = models.ImageField('232446.jpg')