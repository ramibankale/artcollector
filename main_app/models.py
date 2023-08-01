from django.db import models
from django.urls import reverse
from datetime import date

TIMEOFDAY = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('N', 'Night'),
)

# Museum model
class Museum(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('museums_detail', kwargs={'pk': self.id})

# Create your models here.
class Art(models.Model):
    name = models.CharField(max_length=100)
    culture = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    origin = models.CharField(max_length=100)
    # create M:M relationship
    museums = models.ManyToManyField(Museum)

    # Changing this instance method does not impact the database
    # therefore no makemigration is necessary 
    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'art_id': self.id})
    
    def listed_for_today(self):
        return self.display_set.filter(date=date.today()).count() >= len(TIMEOFDAY)
    
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

    