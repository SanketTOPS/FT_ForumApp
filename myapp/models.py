from django.db import models

# Create your models here.

class signup_master(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=12)
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    zipcode=models.IntegerField()


class mynotes(models.Model):
    uploaded=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100)
    cate=models.CharField(max_length=100)
    myfiles=models.FileField(upload_to="MyFiles")
    comments=models.TextField()

class contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    subject=models.CharField(max_length=20)
    msg=models.TextField()


    