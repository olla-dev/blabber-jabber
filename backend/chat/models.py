from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class ChatRoom(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    description = models.TextField()
    users = models.ManyToManyField(User, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['name', 'id'], name='name_idx')
        ]
        ordering = ['-updated_at']
    def __str__(self):
        return "%s: %s" % (self.name, self.description)

class Message(models.Model):

    class MessageStatus(models.TextChoices):
            SENT = 'SENT', _('Sent')
            READ = 'READ', _('Read')
            DELETED = 'DELETED', _('Deleted')
            
    sent_time_utc = models.DateTimeField(null=False, blank=False)
    content = models.TextField()
    status = models.CharField(max_length=7,
        choices=MessageStatus.choices,
        default=MessageStatus.SENT)
    author = models.ForeignKey(
        User, 
        related_name="messages",
        on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        ChatRoom, 
        related_name="messages",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['sent_time_utc', 'id'], name='sent_time_utc_idx')
        ]
        ordering = ['-sent_time_utc']
    
    def __str__(self):
        return "Message %s (%s): %s" % (self.user.id, self.sent_time_utc, self.content)