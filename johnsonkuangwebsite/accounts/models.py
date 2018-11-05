from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from website.models import NewsletterUser


# Create your models here.
class Profile(models.Model):
    EXPERIENCE_CHOICES = (
        ('IB', 'IB'),
        ('AP', 'AP'),
        ('Running Start', 'Running Start'),
        ('Honors', 'Honors'),
        ('Gen Ed', 'Gen Ed'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    newsletter = models.ForeignKey(NewsletterUser, on_delete=models.SET_NULL, blank=True, null=True)
    subscribed = models.BooleanField(default=False)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)

    birth_date = models.DateField(null=True, blank=True)
    career = models.CharField(max_length=250, blank=True)
    school = models.CharField(max_length=255, blank=True)
    experience = models.CharField(max_length=40, choices=EXPERIENCE_CHOICES)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        p = Profile.objects.create(user=instance)
        if NewsletterUser.objects.filter(email=p.email).exists():
            if p.subscribed:
                n = NewsletterUser.objects.get(email=p.email)
                p.newsletter = n
        else:
            if p.subscribed:
                n = NewsletterUser.objects.created(email=p.email)
                p.newsletter=n
        p.save()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

