from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

# @receiver(post_save, sender=Profile)
def createProfile(sender,instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            users = user,
            username = user.username,
            email = user.email,
            name = user.first_name
        )

def profileDeleted(sender,instance, **kwargs):
    print("Profile Deleted!")

post_save.connect(createProfile, sender = User)
post_delete.connect(profileDeleted, sender = Profile)