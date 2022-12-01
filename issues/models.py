from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

class Issue(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,blank=True,default=1
    )
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('detailIssue', args=[self.id])

