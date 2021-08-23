from django.urls import path
from .views import CertificationListCreateAPIView

urlpatterns = [
    path('certifications', CertificationListCreateAPIView.as_view(), name='create-certifications')

]
app_name = 'certifications'