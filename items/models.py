from django.db import models
from django.urls import reverse


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Items(models.Model):
    title = models.CharField(max_length=256)
    price = models.DecimalField(decimal_places=2, max_digits= 10)
    description = models.CharField(max_length=512)
    image = models.ImageField(blank=True, upload_to="images/") 
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        blank = True,
        null = True
    )


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])

