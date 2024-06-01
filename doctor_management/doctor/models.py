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

class Department(models.Model):
    department_name = models.CharField(max_length=100)  # Thay đổi tên trường thành department_name

    def __str__(self):
        return self.department_name

class Account(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)  # Note: Password cần phải được mã hóa

    def __str__(self):
        return self.username

class Doctor(models.Model):
    fullname = models.OneToOneField(FullName, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)  # Thay đổi OneToOneField thành ForeignKey
    account = models.OneToOneField(Account, on_delete=models.CASCADE)  # Liên kết với Account
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    working_hours = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='doctor_images/')
    status = models.CharField(max_length=20)

    def __str__(self):
        return str(self.fullname)
