from django.db import models

# Create your models here.

from division.models import Divisions 


class division(models.Model):
    name = models.CharField(max_length=400)
    div_id = models.ForeignKey(Divisions,models.CASCADE)


