from django.db import models
from django.urls import reverse

# Create your models here.

class Items(models.Model):
    title = models.CharField(max_length=256)
    price = models.DecimalField(decimal_places=2, max_digits= 4)
    description = models.CharField(max_length=512)
    image = models.ImageField(blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])

