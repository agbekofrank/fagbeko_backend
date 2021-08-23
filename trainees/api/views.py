from django.db.models.query import QuerySet
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, DestroyAPIView,UpdateAPIView,
    CreateAPIView, RetrieveUpdateAPIView
    )
from rest_framework import parsers
from trainees.models import Trainee
from .serializers import TraineeSerializer, TraineeDetailSerializer, TraineeCreateSerializer

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
    