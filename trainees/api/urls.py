from django.urls import path
from .views import (
    TraineeCreateAPIView, 
    TraineeListAPIView,
    TraineeDetailAPIView,
    TraineeEditAPIView,
    TraineeDeleteAPIView
    )


urlpatterns = [
    path('create/', TraineeCreateAPIView.as_view(), name='create'),
    path('<int:id>/', TraineeDetailAPIView.as_view(), name='detail'),
    path('<int:id>/edit/', TraineeEditAPIView.as_view(), name='edit'),
    # # path('<str:slug>/update/', PostUpdateAPIView.as_view(), name='update'),
    path('<int:id>/delete/', TraineeDeleteAPIView.as_view(), name='delete'),
    path('', TraineeListAPIView.as_view(), name='trainees'),
]
app_name = 'trainees'