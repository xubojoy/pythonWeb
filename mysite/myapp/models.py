from django.db import models

# Create your models here.
class Person(models.Model):
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
    SHIRT_SIZES = (
        ('s','Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60,default='xubojoy')
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES,default='M')
