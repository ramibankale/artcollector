from django.db import models
from django.urls import reverse


# Create your models here.
class Art(models.Model):
    name = models.CharField(max_length=100)
    culture = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    origin = models.CharField(max_length=100)

    # Changing this instance method does not impact the database
    # therefore no makemigration is necessary 
    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'art_id': self.id})