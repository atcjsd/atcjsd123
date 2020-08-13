from django.db import models

class User(models.Model):
    name = models.CharField(max_length=10)
    id = models.CharField(primary_key=True, max_length=20)
    pwd = models.CharField(max_length=16)
    birth = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    image = models.ImageField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)