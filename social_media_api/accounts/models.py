from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.conf import settings

class CustomerUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='following',
        symmetrical=False,
        blank=True
    )
    groups = models.ManyToManyField(Group, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission,related_name='customuser_set_permissions',blank=True)

    def __str__(self):
        return self.email