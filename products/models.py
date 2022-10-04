from email.policy import default
from django.db import models
class Product(models.Model):
    title = models.CharField(max_length=50,)
    description = models.TextField(blank = True, null = True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(blank = False, null = False)
    featured = models.BooleanField(default=False)