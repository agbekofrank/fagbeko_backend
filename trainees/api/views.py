from django.db.models.query import QuerySet
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, DestroyAPIView,UpdateAPIView,
    CreateAPIView, RetrieveUpdateAPIView
    )
from rest_framework import parsers
from trainees.models import Trainee
from .serializers import TraineeSerializer, TraineeDetailSerializer

class TraineeDetailAPIView(RetrieveAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeDetailSerializer
    lookup_field = 'id'

class TraineeCreateAPIView(CreateAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer
    parser_classes = [parsers.MultiPartParser]


class TraineeListAPIView(ListAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer
    