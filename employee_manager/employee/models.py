from django.db import models

class FullName(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Address(models.Model):
    street = models.CharField(max_length=100)
    numberhouse = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.street}, {self.numberhouse}'

class Employee(models.Model):
    name = models.ForeignKey(FullName, on_delete=models.CASCADE)
    department = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
