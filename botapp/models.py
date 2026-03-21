from django.db import models


class BotUser(models.Model):
    chat_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=255, blank=True,null=True)
    last_name = models.CharField(max_length=255, blank=True,null=True)
    username = models.CharField(max_length=255, blank=True,null=True)
    is_active = models.BooleanField(default=True)

    joined_at = models.DateTimeField(auto_now_add=True)

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name if self.last_name else self.first_name
    
    def __str__(self):
        return self.first_name + " " + self.last_name if self.last_name else self.first_name