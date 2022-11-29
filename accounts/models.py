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