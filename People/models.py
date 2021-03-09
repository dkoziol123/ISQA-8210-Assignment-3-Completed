from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class People(models.Model):

    name = models.CharField(max_length=50,blank=False, null=False, default=' ')
    email = models.CharField(max_length=50, default=' ')
    phone = models.CharField(max_length=50,default='(402)000-0000')
    notes = models.TextField()

    author = models.ForeignKey(
        get_user_model(),
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('people_detail', args=[str(self.id)])

#class Comment(models.Model):
    #people = models.ForeignKey(
        #People,
        #on_delete=models.CASCADE,
        #related_name='comments',
    #)
    #comment = models.CharField(max_length=140)
    #author = models.ForeignKey(
        #get_user_model(),
        #on_delete=models.CASCADE,
   # )

    #def __str__(self):
        #return self.comment

    #def get_absolute_url(self):
        #return reverse('people_list')

