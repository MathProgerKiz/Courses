from rest_framework import serializers

from Certificates.models import CertificatesModel


class CertificateSerializers(serializers.ModelSerializer):
    class Meta:
        model=CertificatesModel
        fields='__all__'
