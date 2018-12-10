from django.db import models
import datetime 
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
	roll_no=models.CharField(max_length=15,primary_key=True,default = "20160010145")

class FacultyAdvisor(models.Model):
	roll_no=models.CharField(max_length=50,primary_key=True)