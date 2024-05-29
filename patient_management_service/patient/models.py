from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=100)
    numberhouse = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.street}, {self.numberhouse}'

class FullName(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Patient(models.Model):
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    fullname = models.OneToOneField(FullName, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.fullname}, {self.address}'
