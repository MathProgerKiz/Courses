from django.urls import path, include
from rest_framework_nested import routers

from Certificates.views import CertificatesViewSet

router = routers.SimpleRouter()
router.register(r'user',CertificatesViewSet , basename='assignments')

certificate_router = routers.NestedSimpleRouter(router, r'user', lookup='user')
certificate_router.register(r'certificate', CertificatesViewSet, basename='user-certificate')

urlpatterns = [
    path('', include(router.urls)),  # Основные маршруты
    path('', include(certificate_router.urls)),  # Вложенные маршруты
]
