from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicineViewSet, CategoryViewSet, SupplyViewSet

router = DefaultRouter()
router.register(r'medicines', MedicineViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'supplies', SupplyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
