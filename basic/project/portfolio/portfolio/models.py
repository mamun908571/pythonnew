from django.db import models


class About(models.Model):
    Name = models.CharField(max_length=500)
    Birthday = models.CharField(max_length=500)
    Phone = models.CharField(max_length=500)
    Email = models.CharField(max_length=500)
    No_Years_of_Experiences = models.CharField(max_length=500)
    No_Happy_Customers = models.CharField(max_length=500)
    No_Project_Finished = models.CharField(max_length=500)
    No_Digital_Awards = models.CharField(max_length=5000)
    description = models.TextField(max_length=5000) 
    date_time = models.CharField(max_length=500)
    v_c = models.CharField(max_length=500)
    v_status = models.CharField(max_length=10)


class Companies(models.Model):
    image = models.ImageField (null = True,blank = True, upload_to = "images/")