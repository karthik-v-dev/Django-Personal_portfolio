from django.db import models

import datetime

class Blog(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    date = models.DateField(default=datetime.date.today)
 
    def __str__(self):
       return self.title

# Create your models here.

