from django.db import models
from django.urls import reverse  # Import the reverse function

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('item_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
