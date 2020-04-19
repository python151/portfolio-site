from django.db import models

# Create your models here.
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)