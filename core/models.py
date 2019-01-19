from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=300)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    follows = models.ManyToManyField("self", related_name="follows", symmetrical=False)
    followers = models.ManyToManyField("self", related_name="followers", symmetrical=False)
    
