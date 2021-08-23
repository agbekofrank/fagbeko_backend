from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, DestroyAPIView,UpdateAPIView,
    CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView
    )
from rest_framework import parsers
from certifications.models import Certification
from .serializers import CertificationSerializer

class CertificationListCreateAPIView(ListCreateAPIView):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
    parser_classes = [parsers.MultiPartParser]