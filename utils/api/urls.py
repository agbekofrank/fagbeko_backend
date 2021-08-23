from django.urls import path
from .views import (
    FieldsListCreateAPIView, 
    EstablishmentListCreateAPIView,
    ExperienceListCreateAPIView,
    EducationListCreateAPIView
    )

urlpatterns = [
    path('fields', FieldsListCreateAPIView.as_view(), name='create-field'),
    path('establishment', EstablishmentListCreateAPIView.as_view(), name='create-establishment'),
    path('education', EducationListCreateAPIView.as_view(), name='create-education'),
    path('experience', ExperienceListCreateAPIView.as_view(), name='create-experience'),

]
app_name = 'utils'