from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

# class Admin(models.Model):
#     first_name = models.CharField(max_length = 128)
#     last_name = models.CharField(max_length = 128)
#
#     email = models.EmailField(unique = True, blank = False)
#     password = models.PasswordField(max_length = 225)


class Role(models.Model):
    role = models.CharField(max_length = 128)

    def __str__(self):
        return self.role


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    admin = models.ForeignKey(User, related_name = 'admin', on_delete = models.CASCADE)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        UserProfile.objects.create(user=instance,role_id = Role.objects.get(role = 'admin').id,
        admin_id = instance.id)

# class PendingInvitation(models.Model):
#     email = models.EmailField()
#     role = models.ForeignKey(Role, on_delete = models.CASCADE)
#     code = models.CharField(max_length = 128)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.is_superuser:
#         instance.userprofile.save()
