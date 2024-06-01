from rest_framework import serializers
from .models import Doctor, FullName, Address, Account, Department

class FullNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullName
        fields = ['first_name', 'last_name']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'numberhouse']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'password']  # Bạn có thể muốn loại trường `password` ra khỏi serialization khi trả về

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id','department_name']

class DepartmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class DepartmentNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['department_name', 'id']
class DoctorSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    fullname = FullNameSerializer()
    account = AccountSerializer()
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())



    class Meta:
        model = Doctor
        fields = '__all__'

    def create(self, validated_data):
        fullname_data = validated_data.pop('fullname')
        address_data = validated_data.pop('address')
        account_data = validated_data.pop('account')
        department_data = validated_data.pop('department')

        name_instance = FullName.objects.create(**fullname_data)
        address_instance = Address.objects.create(**address_data)
        account_instance = Account.objects.create(**account_data)
        department_id = department_data.id
        doctor_instance = Doctor.objects.create(fullname=name_instance, address=address_instance, account=account_instance, department_id=department_id, **validated_data)
        return doctor_instance

    def update(self, instance, validated_data):
        fullname_data = validated_data.pop('fullname')
        address_data = validated_data.pop('address')
        account_data = validated_data.pop('account')
        department_id = validated_data.pop('department')

        # Update FullName instance
        instance.fullname.first_name = fullname_data.get('first_name', instance.fullname.first_name)
        instance.fullname.last_name = fullname_data.get('last_name', instance.fullname.last_name)
        instance.fullname.save()

        # Update Address instance
        instance.address.street = address_data.get('street', instance.address.street)
        instance.address.numberhouse = address_data.get('numberhouse', instance.address.numberhouse)
        instance.address.save()

        # Update Account instance
        instance.account.username = account_data.get('username', instance.account.username)
        instance.account.password = account_data.get('password', instance.account.password)
        instance.account.save()

        # Update Department instance
        instance.department_id = department_id
        instance.save()

        # Update Doctor instance
        instance.specialization = validated_data.get('specialization', instance.specialization)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.email = validated_data.get('email', instance.email)
        instance.working_hours = validated_data.get('working_hours', instance.working_hours)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        return instance
