
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('trainees/api/', include('trainees.api.urls', namespace='trainees-api')),
    path('accounts/api/', include('accounts.api.urls', namespace='accounts-api')),
    path('utils/api/', include('utils.api.urls', namespace='utils-api')),
    path('certifications/api/', include('certifications.api.urls', namespace='certifications-api')),
    path('skills/api/', include('skills.api.urls', namespace='skill-api'))

]
