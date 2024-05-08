from django.db import models

# Create your models here.
class Library(models.Model):
    bookid=models.IntegerField(primary_key=True)
    bookname=models.CharField(max_length=200)
    customername =models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    phonenumber=models.CharField(max_length=200)