# views.py
from rest_framework import generics
from .models import Clinic, Bed
from .serializers import ClinicSerializer, BedSerializer

class ClinicListCreateAPIView(generics.ListCreateAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

class ClinicRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

class BedListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer

class BedRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
