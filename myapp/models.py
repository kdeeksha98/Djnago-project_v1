from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length = 100)
    quantity = models.IntegerField(default = 15)
    author_name = models.CharField(max_length = 200)
    release_year = models.DateField()
    description = models.CharField(max_length = 500)
