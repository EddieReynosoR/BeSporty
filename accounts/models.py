from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=70, unique=True)
    address = models.CharField(max_length=128, blank=True)
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        blank = True,
        null = True
    )
    auth_token = models.CharField(max_length=100, default=False)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username