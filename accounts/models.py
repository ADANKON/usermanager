from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return self.username