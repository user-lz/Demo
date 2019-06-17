# models.py
from django.db import models
 
class Test(models.Model):
    movie_id= models.CharField(max_length=10)
    movie_name= models.CharField(max_length=20)

class Phones(models.Model):
    pNo = models.CharField(max_length=7)
    pBrand = models.CharField(max_length=100)
    pPrice = models.CharField(max_length=20)
    pContent = models.CharField(max_length=100)
    pFile = models.CharField(max_length=20)
class User(models.Model):
    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)  