from django.urls import path
from .views import (
    TraineeCreateAPIView, 
    TraineeListAPIView,
    TraineeDetailAPIView,
    TraineeEditAPIView,
    TraineeDeleteAPIView,
    FieldsListCreateAPIView, 
    EstablishmentListCreateAPIView,
    ExperienceListCreateAPIView,
    EducationListCreateAPIView,
    CertificationListCreateAPIView,
    SkillListCreateAPIView
    )


urlpatterns = [
    path('create/', TraineeCreateAPIView.as_view(), name='create'),
    path('<int:id>/', TraineeDetailAPIView.as_view(), name='detail'),
    path('<int:id>/edit/', TraineeEditAPIView.as_view(), name='edit'),
    # # path('<str:slug>/update/', PostUpdateAPIView.as_view(), name='update'),
    path('fields', FieldsListCreateAPIView.as_view(), name='create-field'),
    path('establishment', EstablishmentListCreateAPIView.as_view(), name='create-establishment'),
    path('education', EducationListCreateAPIView.as_view(), name='create-education'),
    path('experience', ExperienceListCreateAPIView.as_view(), name='create-experience'),
    path('<int:id>/delete/', TraineeDeleteAPIView.as_view(), name='delete'),
    path('', TraineeListAPIView.as_view(), name='trainees'),
    path('certifications', CertificationListCreateAPIView.as_view(), name='create-certifications'),
    path('skills', SkillListCreateAPIView.as_view(), name='create-skills')


]
app_name = 'trainees'