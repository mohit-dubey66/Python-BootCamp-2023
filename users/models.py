from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.base import Model
from django.db.models.signals import post_save
# Create your models here.

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver



class Profile(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    username = models.CharField(max_length=200,blank=True,null=True)
    location = models.CharField(max_length=200,blank=True,null=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(max_length=254,blank=True,null=True)
    short_intro = models.CharField(max_length=200,blank=True,null=True)
    bio = models.CharField(max_length=200,blank=True,null=True)
    profile_image = models.ImageField(null=True, blank = True, upload_to='profiles/', default = 'profiles/user.png')
    social_github = models.CharField(max_length=200,blank=True,null=True)
    social_linkedin = models.CharField(max_length=200,blank=True,null=True)
    social_twitter = models.CharField(max_length=200,blank=True,null=True)
    social_youtube = models.CharField(max_length=200,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True ,editable=False)
    
    def __str__(self):
        return str(self.username)
    

class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True ,editable=False)


    def __str__(self):
        return str(self.name)

