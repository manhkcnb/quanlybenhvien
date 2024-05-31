# medical_records/views.py
import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import MedicalRecord
from .serializers import MedicalRecordSerializer

PATIENT_SERVICE_URL = 'http://127.0.0.1:8006/api/patients/'
DOCTOR_SERVICE_URL = 'http://127.0.0.1:8003/api/doctors/'

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer

    def get_patient_info(self, patient_id):
        response = requests.get(f'{PATIENT_SERVICE_URL}{patient_id}')
        if response.status_code == 200:
            return response.json()
        return {}

    def get_doctor_info(self, doctor_id):
        response = requests.get(f'{DOCTOR_SERVICE_URL}{doctor_id}')
        if response.status_code == 200:
            return response.json()
        return {}

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['get'])
    def patients_list(self, request):
        response = requests.get(PATIENT_SERVICE_URL)
        if response.status_code == 200:
            return Response(response.json())
        return Response(status=response.status_code)

    @action(detail=False, methods=['get'])
    def doctors_list(self, request):
        response = requests.get(DOCTOR_SERVICE_URL)
        if response.status_code == 200:
            return Response(response.json())
        return Response(status=response.status_code)
