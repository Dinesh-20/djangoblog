from django.db.models.signals import post_save  # Called When a model is saved
from django.contrib.auth.models import User    # Normal user model import
from django.dispatch import receiver    # To identify the receiver of the save
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


# @receiver(post_save, sender=User)
# def create_about(sender, instance, created, **kwargs):
#     if created:
#         About.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_about(sender, instance, **kwargs):
#     instance.about.save()
