from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import PatientViewSet, DoctorViewSet, MappingViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'mappings', MappingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('api/', include(router.urls)),
]
