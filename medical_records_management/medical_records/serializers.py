# medical_records/serializers.py
from rest_framework import serializers
from .models import MedicalRecord, Medication

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ['id', 'name', 'dosage', 'frequency']

class MedicalRecordSerializer(serializers.ModelSerializer):
    medications = MedicationSerializer(many=True)
    patient_info = serializers.SerializerMethodField()
    doctor_info = serializers.SerializerMethodField()

    class Meta:
        model = MedicalRecord
        fields = ['id', 'patient_id', 'patient_info', 'doctor_id', 'doctor_info', 'visit_date', 'diagnosis', 'treatment', 'medications', 'notes']

    def get_patient_info(self, obj):
        response = requests.get(f'http://127.0.0.1:8006/api/patients/{obj.patient_id}')
        return response.json() if response.status_code == 200 else {}

    def get_doctor_info(self, obj):
        response = requests.get(f'http://127.0.0.1:8003/api/doctors/{obj.doctor_id}')
        return response.json() if response.status_code == 200 else {}

    def create(self, validated_data):
        medications_data = validated_data.pop('medications')
        record = MedicalRecord.objects.create(**validated_data)
        for med_data in medications_data:
            med, created = Medication.objects.get_or_create(**med_data)
            record.medications.add(med)
        return record

    def update(self, instance, validated_data):
        medications_data = validated_data.pop('medications')
        instance.patient_id = validated_data.get('patient_id', instance.patient_id)
        instance.doctor_id = validated_data.get('doctor_id', instance.doctor_id)
        instance.visit_date = validated_data.get('visit_date', instance.visit_date)
        instance.diagnosis = validated_data.get('diagnosis', instance.diagnosis)
        instance.treatment = validated_data.get('treatment', instance.treatment)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.save()

        instance.medications.clear()
        for med_data in medications_data:
            med, created = Medication.objects.get_or_create(**med_data)
            instance.medications.add(med)
        return instance
