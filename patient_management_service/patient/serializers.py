from rest_framework import serializers
from .models import Patient
from .models import Address
from .models import FullName


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'numberhouse']

class FullNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullName
        fields = ['first_name', 'last_name']

class PatientSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    fullname = FullNameSerializer()

    class Meta:
        model = Patient
        fields = ['id', 'address', 'fullname', 'date_of_birth', 'gender', 'phone_number']
    def create(self, validated_data):
        address_data = validated_data.pop('address')
        fullname_data = validated_data.pop('fullname')
        address = Address.objects.create(**address_data)
        fullname = FullName.objects.create(**fullname_data)
        patient = Patient.objects.create(address=address, fullname=fullname, **validated_data)
        return patient
    def update(self, instance, validated_data):
        address_data = validated_data.pop('address', None)
        fullname_data = validated_data.pop('fullname', None)

        if address_data:
            address_serializer = AddressSerializer(instance.address, data=address_data)
            if address_serializer.is_valid():
                address_serializer.save()

        if fullname_data:
            fullname_serializer = FullNameSerializer(instance.fullname, data=fullname_data)
            if fullname_serializer.is_valid():
                fullname_serializer.save()

        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()

        return instance

    def delete(self, instance):
        instance.address.delete()
        instance.fullname.delete()
        instance.delete()
