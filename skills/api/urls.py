from django.urls import path
from .views import SkillListCreateAPIView

urlpatterns = [
    path('skills', SkillListCreateAPIView.as_view(), name='create-skills')

]
app_name = 'skills'