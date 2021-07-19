from django.db import models

class User(models.Model):
    creation_time = models.DateTimeField('last time fetched')
    username = models.CharField(max_length=100)
    xml_data = models.TextField()