from django.db import models
from django.urls import reverse


# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)

def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('book_edit',kwargs={'pk':self.pk})