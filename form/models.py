from django.db import models
from datetime import datetime
# Create your models here.

class Info(models.Model):
    Student_Name=models.CharField(max_length=100)
    Father_Name=models.CharField(max_length=100)
    Mother_Name=models.CharField(max_length=100)
    Date_Of_Birth=models.DateField(null=True)
    gender=models.CharField(max_length=100, null=True)
    roll=models.CharField(max_length=100)
    branch=models.CharField(max_length=100, null=True)
    year=models.CharField(max_length=100, null=True)
    Contact_Number=models.CharField(max_length=100,null=True)
    Father_Contact_Number=models.CharField(max_length=100,null=True)
    Mother_Contact_Number=models.CharField(max_length=100, null=True)
    Aadhar_Number=models.CharField( max_length=100,null=True)
    Address=models.TextField(null=True)



    def __str__(self):
        return self.Student_Name
    