from rest_framework import serializers
from .models import Medicine,Category, Supply

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = ['id', 'name', 'medicine', 'quantity', 'supply_date', 'expiration_date', 'cost', 'batch_number']
