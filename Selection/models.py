from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Selection(models.Model):

    Preference = models.CharField(max_length=50, blank=False, null=False, default=' ') #will be _type pk from Type
    Budget_Dollar = models.PositiveIntegerField(blank=False, null=True, default=' 5')
    Time_Frame_Hour = models.PositiveIntegerField(default=' 5')

    #would like to add 'author' as person from People as a nice to have
    # state = models.CharField(max_length=50, default='NE')


    def __str__(self):
        return self.Preference

    def get_absolute_url(self):
        return reverse('selection_detail', args=[str(self.id)])

#class Comment(models.Model):
    #client = models.ForeignKey(
        #Client,
        #on_delete=models.CASCADE,
        #related_name='comments',
    #)
    #comment = models.CharField(max_length=140)
    #author = models.ForeignKey(
     #   get_user_model(),
     #   on_delete=models.CASCADE,
    #)

    #def __str__(self):
    #    return self.comment

    #def get_absolute_url(self):
     #   return reverse('Client_list')

