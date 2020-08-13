from django.db import models

class articlebuy(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    image = models.ImageField(blank=True,upload_to="image",null=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

class articlefree(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    image = models.ImageField(blank=True,upload_to="image",null=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

class articlesale(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    image = models.ImageField(blank=True,upload_to="image",null=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

class articlenotic(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
