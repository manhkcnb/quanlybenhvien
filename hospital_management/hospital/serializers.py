from rest_framework import serializers
from .models import Doctor, FullName, Address

class FullNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullName
        fields = ['first_name', 'last_name']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'numberhouse']

class DoctorSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    fullname = FullNameSerializer()

    class Meta:
        model = Doctor
        fields = '__all__'

    def create(self, validated_data):
        fullname_data = validated_data.pop('fullname')
        address_data = validated_data.pop('address')

        name_instance = FullName.objects.create(**fullname_data)
        address_instance = Address.objects.create(**address_data)
        
        doctor_instance = Doctor.objects.create(fullname=name_instance, address=address_instance, **validated_data)
        return doctor_instance

    def update(self, instance, validated_data):
        fullname_data = validated_data.pop('fullname')
        address_data = validated_data.pop('address')
        
        instance.first_name = fullname_data.get('first_name', instance.first_name)
        instance.last_name = fullname_data.get('last_name', instance.last_name)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
