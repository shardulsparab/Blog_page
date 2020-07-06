from django.db import models
import datetime

# Create your models here.
class login(models.Model):
    Name=models.CharField(max_length=30)
    Password = models.CharField(max_length=20)
    ReEnterPassword=models.CharField(max_length=20)
    Email = models.EmailField(max_length=30)

    def __str__(self):
        return self.Name

# Create your models here.

class createblog(models.Model):
    Author_Name = models.CharField(max_length=30)
    places=models.CharField(max_length=30)
    date = models.DateField()
    content_blog=models.CharField(max_length=1000)
    picture=models.ImageField(upload_to='images/')
