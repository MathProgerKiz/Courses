
# Create your views here.
from rest_framework import viewsets

from Certificates.models import CertificatesModel
from Certificates.permissions import IsLector
from Certificates.serializers import CertificateSerializers


class CertificatesViewSet(viewsets.ModelViewSet):
    serializer_class = CertificateSerializers
    permission_classes = (IsLector,)

    def get_queryset(self):
        """Метод для получения пользователя по id"""
        user_id = self.kwargs.get('user__id')
        if (user_id):
            return CertificatesModel.objects.get(user_id=user_id)
        else:
            return CertificatesModel.objects.all()
