from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

# Create your models here.
from django.dispatch import receiver


class Skill(models.Model):
    skill_name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ('skill_name', )
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.skill_name


class Project(models.Model):
    project_title = models.CharField(max_length=200, )
    description = models.TextField(max_length=255, )
    img_1 = models.ImageField(upload_to='images/', blank=True, null=True)
    img_2 = models.ImageField(upload_to='images/', blank=True, null=True)
    img_3 = models.ImageField(upload_to='images/', blank=True, null=True)
    img_4 = models.ImageField(upload_to='images/', blank=True, null=True)
    img_5 = models.ImageField(upload_to='images/', blank=True, null=True)
    date_started = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(auto_now_add=True)
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_completed', )

    def __str__(self):
        return self.project_title


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone_number = models.CharField(max_length=13, null=True)
    secondary_email = models.EmailField()
    profile_image = models.ImageField(upload_to='images/profile', null=True, blank=True)

    def __str__(self):
        return self.phone_number


@receiver(post_save, sender=User)
def create_profile(sender, instance, created , **kwargs):
    user_profile = UserProfile.objects.get_or_create(user=instance)
    user_profile.save()
