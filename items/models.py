from django.db import models
from django.urls import reverse

class Items(models.Model):
    title = models.CharField(max_length=256)
    price = models.DecimalField(decimal_places=2, max_digits= 10)
    description = models.CharField(max_length=512)
    image = models.ImageField(blank=True, upload_to="images/")


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])

