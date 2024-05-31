import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Appointment
from .serializers import AppointmentSerializer

PATIENT_SERVICE_URL = 'http://127.0.0.1:8006/api/patients/'
DOCTOR_SERVICE_URL = 'http://127.0.0.1:8003/api/doctors/'
ROOM_SERVICE_URL = 'http://127.0.0.1:8004/api/clinics/'

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_doctors_list(self):
        response = requests.get(DOCTOR_SERVICE_URL)
        if response.status_code == 200:
            return response.json()
        return []

    def get_patients_list(self):
        response = requests.get(PATIENT_SERVICE_URL)
        if response.status_code == 200:
            return response.json()
        return []

    def get_rooms_list(self):
        response = requests.get(ROOM_SERVICE_URL)
        if response.status_code == 200:
            return response.json()
        return []

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
    def doctors_list(self, request):
        doctors = self.get_doctors_list()
        return Response(doctors)

    @action(detail=False, methods=['get'])
    def patients_list(self, request):
        patients = self.get_patients_list()
        return Response(patients)

    @action(detail=False, methods=['get'])
    def rooms_list(self, request):
        rooms = self.get_rooms_list()
        return Response(rooms)
