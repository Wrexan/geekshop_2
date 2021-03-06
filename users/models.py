from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.dispatch import receiver
from django.db.models.signals import post_save

from datetime import timedelta


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
    activation_key = models.CharField(max_length=128, blank=True)

    @property
    def is_activation_key_expired(self):
        res = now() - self.date_joined > timedelta(hours=48)
        message = '' if not res else \
            f'Сейчас: {now()}\n' \
            f'Дата регистрации: {self.date_joined}\n' \
            f'Прошло {now() - self.date_joined}\n' \
            f'Допустимое время: {timedelta(hours=48)}'
        return res, message

    def safe_delete(self):
        self.is_active = False
        self.save()


class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'
    OTHER = 'X'

    GENDER_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'Ж'),
        (OTHER, 'Х')
    )

    user = models.OneToOneField(
        User, unique=True, null=False, db_index=True, on_delete=models.CASCADE
    )

    tagline = models.CharField(verbose_name='тэги', max_length=128, blank=True)
    about_me = models.TextField(verbose_name='о себе', max_length=512, blank=True)
    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER_CHOICES, blank=True)

    @receiver(post_save, sender=User)
    def user_profile_saved(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
        instance.userprofile.save()
