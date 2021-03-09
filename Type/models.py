from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Type(models.Model):
    Recreation_Name = models.CharField(max_length=50)
    Recreation_Type_Indoor = models.CharField(max_length=50)
    Recreation_Type_Outdoor = models.CharField(max_length=50)
    Public = models.CharField(max_length=3)
    Private = models.CharField(max_length=3)

    _type = models.ForeignKey(
        get_user_model(),
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.Recreation_Name

    def get_absolute_url(self):
        return reverse('type_detail', args=[str(self.id)])




