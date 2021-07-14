from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.

class User(models.Model):
    creation_time = models.DateTimeField('last time fetched')
    username = models.CharField(max_length=200)
    xml_data = TextField()