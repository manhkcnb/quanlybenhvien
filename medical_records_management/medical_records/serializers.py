from rest_framework import serializers
from .models import MedicalRecord, Medication, Treatment, MedicalHistory
import requests

class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = '__all__'

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'

class MedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = '__all__'

class MedicalRecordSerializer(serializers.ModelSerializer):
    patient_info = serializers.SerializerMethodField()
    doctor_info = serializers.SerializerMethodField()
    medications_info = serializers.SerializerMethodField()
    treatments = TreatmentSerializer(many=True, read_only=True)
    medications = MedicationSerializer(many=True, read_only=True)
    medical_history = MedicalHistorySerializer(read_only=True)

    class Meta:
        model = MedicalRecord
        fields = [
            'id', 'patient_id', 'patient_info', 'doctor_id', 'doctor_info', 
            'visit_date', 'diagnosis', 'treatments', 'medications', 'notes', 
            'medications_info', 'medical_history'
        ]
        read_only_fields = ['id', 'medications_info']

    def get_patient_info(self, obj):
        patient_id = obj.patient_id
        patient_info = self._get_api_data(f'http://127.0.0.1:8006/api/patients/{patient_id}')
        return patient_info

    def get_doctor_info(self, obj):
        doctor_id = obj.doctor_id
        doctor_info = self._get_api_data(f'http://127.0.0.1:8003/api/doctors/{doctor_id}')
        return doctor_info

    def get_medications_info(self, obj):
        return obj.medications_info

    def _get_api_data(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {url}: {e}")
            return {}
        except ValueError as e:
            print(f"Error decoding JSON from {url}: {e}")
            return {}

    def create(self, validated_data):
        treatments_data = validated_data.pop('treatments')
        medical_record = MedicalRecord.objects.create(**validated_data)
        
        for treatment_data in treatments_data:
            Treatment.objects.create(medical_record=medical_record, **treatment_data)
        
        return medical_record

    def update(self, instance, validated_data):
        treatments_data = validated_data.pop('treatments')
        
        # Update treatments
        instance.treatments.all().delete()  # Delete existing treatments
        for treatment_data in treatments_data:
            Treatment.objects.create(medical_record=instance, **treatment_data)
        
        # Update other fields of MedicalRecord
        instance.patient_id = validated_data.get('patient_id', instance.patient_id)
        instance.doctor_id = validated_data.get('doctor_id', instance.doctor_id)
        instance.appointment_id = validated_data.get('appointment_id', instance.appointment_id)
        instance.visit_date = validated_data.get('visit_date', instance.visit_date)
        instance.diagnosis = validated_data.get('diagnosis', instance.diagnosis)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.save()

        return instance
