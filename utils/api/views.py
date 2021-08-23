from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, DestroyAPIView,UpdateAPIView,
    CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView
    )
from rest_framework import parsers
from utils.models import Fields, Establishment, Education, Experience
from .serializers import (
    FieldsSerializer,
    EstablishmentSerializer, 
    EducationSerializer, 
    ExperienceSerializer
    )


class EducationListCreateAPIView(ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    parser_classes = [parsers.MultiPartParser]
    
class ExperienceListCreateAPIView(ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    parser_classes = [parsers.MultiPartParser]

class FieldsListCreateAPIView(ListCreateAPIView):
    queryset = Fields.objects.all()
    serializer_class = FieldsSerializer
    parser_classes = [parsers.MultiPartParser]

class EstablishmentListCreateAPIView(ListCreateAPIView):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer
    parser_classes = [parsers.MultiPartParser]