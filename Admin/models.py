from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    desc = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Feature(models.Model):
    title = models.CharField(max_length=50)
    img = models.FileField(upload_to='img/', max_length=100)
    desc = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Social_Links(models.Model):
    title = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    link = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name =models.CharField(max_length=50)
    email =models.CharField(max_length=50)
    subject =models.CharField(max_length=50)
    phone =models.CharField(max_length=50)
    desc = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    instagram = models.CharField(max_length=150)
    facebook = models.CharField(max_length=150)
    twitter = models.CharField(max_length=150)
    linkedin = models.CharField(max_length=150)
    desc = models.TextField()
    img = models.FileField(upload_to='team/', max_length=100)

    def __str__(self):
        return self.name
    
class Card(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    img = models.FileField(upload_to='card/', max_length=100)

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    title = models.CharField( max_length=50)
    img = models.FileField(upload_to='portfolio/', max_length=100)
    cat = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title

