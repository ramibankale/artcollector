from django.db import models
from django.urls import reverse

TIMEOFDAY = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('N', 'Night'),
)

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
    
class Display(models.Model):
    date = models.DateField('Display Date')
    timeofday = models.CharField(
        max_length=1,
        choices=TIMEOFDAY,
        default=TIMEOFDAY[0][0]
    )

    art = models.ForeignKey(
        Art, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.get_timeofday_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']