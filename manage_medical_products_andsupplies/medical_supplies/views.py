from rest_framework import generics
from .models import MedicalSupply
from .serializers import MedicalSupplySerializer

class MedicalSupplyListCreateAPIView(generics.ListCreateAPIView):
    queryset = MedicalSupply.objects.all()
    serializer_class = MedicalSupplySerializer

class MedicalSupplyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalSupply.objects.all()
    serializer_class = MedicalSupplySerializer