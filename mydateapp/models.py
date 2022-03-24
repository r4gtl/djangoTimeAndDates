from django.db import models

# Create your models here.

class Times(models.Model):
    my_date = models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()