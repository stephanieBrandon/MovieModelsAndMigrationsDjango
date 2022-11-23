from django.db import models

# Create your models here.
# Null refers to the database side
# black = True refers to the front end so it allows the front end to be null 

class Movie(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def _str_ 
