# serializers.py
from rest_framework import serializers
from .models import Employee, FullName, Address

class FullNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullName
        fields = ['first_name', 'last_name']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'numberhouse']

class EmployeeSerializer(serializers.ModelSerializer):
    name = FullNameSerializer()
    address = AddressSerializer()

    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        name_data = validated_data.pop('name')
        address_data = validated_data.pop('address')

        name = FullName.objects.create(**name_data)
        address = Address.objects.create(**address_data)

        employee = Employee.objects.create(name=name, address=address, **validated_data)
        return employee
