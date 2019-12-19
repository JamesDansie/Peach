from django.db import models

# Create your models here.
class Dish(models.Model):
    title = models.CharField(max_length=200)
    # This is for storing the url to the image
    img = models.CharField(max_length=200)
    restaurant_name = models.CharField(max_length=200)
    # decimal fields can be found here; https://www.geeksforgeeks.org/decimalfield-django-models/
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=200)
    other_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title + ' from ' + self.restaurant_name