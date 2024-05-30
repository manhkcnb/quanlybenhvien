from django.urls import path, include
from medicine.views import MedicineListCreateAPIView, MedicineRetrieveUpdateDestroyAPIView
from medical_supplies.views import MedicalSupplyListCreateAPIView, MedicalSupplyRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/medicine/', MedicineListCreateAPIView.as_view(), name='medicine_list'),
    path('api/medicine/<int:pk>/', MedicineRetrieveUpdateDestroyAPIView.as_view(), name='medicine_detail'),
    path('api/medical-supplies/', MedicalSupplyListCreateAPIView.as_view(), name='medical_supply_list'),
    path('api/medical-supplies/<int:pk>/', MedicalSupplyRetrieveUpdateDestroyAPIView.as_view(), name='medical_supply_detail'),
]