from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, home_redirect

router = DefaultRouter()
router.register(r'patients', PatientViewSet)

urlpatterns = [
     path('', home_redirect),  #
    path('', include(router.urls)),
    
]
