from django.dispatch import receiver
from django_registration.signals import user_activated
from django.db.models.signals import post_save
from django.utils.timezone import now

from .models import Profile
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def build_profile_on_user_creation(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()

@receiver(user_activated, sender=User)
def email_activated(sender, user, request, **kwargs):
    user.profile.email_verified_at = now()