from django.urls import path, include
from medical_supplies.views import MedicalSupplyListCreateAPIView, MedicalSupplyRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/medical-supplies/', MedicalSupplyListCreateAPIView.as_view(), name='medical_supply_list'),
    path('api/medical-supplies/<int:pk>/', MedicalSupplyRetrieveUpdateDestroyAPIView.as_view(), name='medical_supply_detail'),
    path('api/', include('medicine.urls')),
]