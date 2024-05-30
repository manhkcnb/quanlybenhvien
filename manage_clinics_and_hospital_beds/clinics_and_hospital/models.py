# models.py
from django.db import models

class Clinic(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    # Các thuộc tính khác của phòng khám

    def __str__(self):
        return self.name

class Bed(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    is_occupied = models.BooleanField(default=False)
    # Các thuộc tính khác của giường bệnh

    def __str__(self):
        return f"Bed {self.number} at {self.clinic.name}"
