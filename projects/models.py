from django.db import models

# Create your models here.
class Project(models.Model):
  fullname = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  products = models.CharField(max_length=255)
  size = models.CharField(max_length=255)
  quantity = models.IntegerField()
  comment = models.CharField(max_length=255)