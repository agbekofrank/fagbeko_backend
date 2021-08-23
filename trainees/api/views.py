from django.db.models.query import QuerySet
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, DestroyAPIView,UpdateAPIView,
    CreateAPIView, RetrieveUpdateAPIView,ListCreateAPIView
    )
from rest_framework import parsers
from .serializers import *

from trainees.models import *

class SkillListCreateAPIView(ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    parser_classes = [parsers.MultiPartParser]

class CertificationListCreateAPIView(ListCreateAPIView):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
    parser_classes = [parsers.MultiPartParser]

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

class TraineeDetailAPIView(RetrieveAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeDetailSerializer
    lookup_field = 'id'

class TraineeDeleteAPIView(DestroyAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeDetailSerializer
    lookup_field = 'id'

class TraineeEditAPIView(RetrieveUpdateAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeDetailSerializer
    lookup_field = 'id'
    parser_classes = [parsers.MultiPartParser]

class TraineeCreateAPIView(CreateAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeCreateSerializer
    parser_classes = [parsers.MultiPartParser]


class TraineeListAPIView(ListAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer
    