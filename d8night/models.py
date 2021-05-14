from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save

#Extends User class by adding a custom Profile class:
class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Activity(models.Model):
    #Labels/fields
    name = models.CharField(max_length=200)
    description = models.TextField()
    #Categories (must be boolean, to be set by user)
    food = models.BooleanField()
    alcohol = models.BooleanField()
    entertainment = models.BooleanField()
    sports = models.BooleanField()
    adventure = models.BooleanField()
    classes = models.BooleanField()

    def __str__(self):
        return self.name

class Date(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dates')
    activity = models.ManyToManyField(Activity)
    created_at = models.DateTimeField(default=timezone.now)
    zip = models.CharField(max_length=5, default="00000")

    def __str__(self):
        return self.name