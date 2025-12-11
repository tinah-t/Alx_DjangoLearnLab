from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from accounts.models import CustomerUser

User = CustomerUser

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE,related_name='notifications')
    actor = models.ForeignKey(User,on_delete=models.CASCADE,related_name='actions')
    verb = models.CharField(max_length=255)
    target_content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE,null=True,blank=True)
    target_object_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('target_content_type', 'target_object_id')
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        if self.target:
            return f"{self.actor} {self.verb} {self.target}"
        return f"{self.actor} {self.verb}"
