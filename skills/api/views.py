from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, DestroyAPIView,UpdateAPIView,
    CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView
    )
from rest_framework import parsers
from skills.models import Skill
from .serializers import SkillSerializer

class SkillListCreateAPIView(ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    parser_classes = [parsers.MultiPartParser]