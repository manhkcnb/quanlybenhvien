from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    expiration_date = models.DateField()
    manufacturer = models.CharField(max_length=255, blank=True, null=True)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    batch_number = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name