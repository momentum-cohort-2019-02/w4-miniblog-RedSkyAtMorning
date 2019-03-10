from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
import uuid

# Create your models here.
class Blogger(models.Model):
    id - models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    bio = models.TextField

    class Meta:
        ordering = ['name',]

    def get_absolute_url(self):
        return reverse('thisblogger', args=[str(self.id)])

    def __str__(self):
        return '{name} (#{id})'.format(self.name, self.id)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    date = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=100)
    content =  models.TextField
    blogger = models.ForeignKey(Blogger, on_delete=models.SET_NULL, null=True, blank=True)
    parentid = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-date',]

    def get_absolute_url(self):
        return reverse ('thispost', args=[str(self.id)])
    
    def __str__(self):
        return '{0}, {1} (#{3})'.format(self.date, self.title, self.id)

    





