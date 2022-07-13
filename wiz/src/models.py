from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=30, blank=True, null=True, unique=True)
    desc = models.TextField(max_length=600, blank=True, null=True)
    image = models.ImageField(default="default.png")
    created = models.DateTimeField(auto_now_add=True)
    about = models.TextField(max_length=800, blank=True, null=True)
    cell = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    slug = models.SlugField(null=False)
    logo = models.ImageField(default="default.png")
    welcome = models.CharField(blank=True, null=True, default="Welcome", max_length=200)

    def __str__(self):
        return self.company


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)
    image = models.ImageField(default="default.png")
    price = models.FloatField()
    desc = models.TextField(max_length=200, blank=True, null=True)

class Plan(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=25)
    price = models.FloatField()
    desc = models.TextField(max_length=300, blank=True, null=True)



    

class Carroussel(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=50, null=True, blank=True)
    background = models.ImageField(default="default.png")
    desc = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.title


POS_CHOICES = (
        ('RIGHT', 'RIGHT'),
        ('LEFT', 'LEFT'),
        ('NOIMAGE', 'NOIMAGE')
    )


class Separator(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=30)
    desc = models.TextField(max_length=800)
    image = models.ImageField(default="default.png")
    place = models.CharField(max_length=8, choices=POS_CHOICES, default='RIGHT')

    def __str__(self):
        return self.title

class Employer(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    funcion = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(default="default.png")
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name











