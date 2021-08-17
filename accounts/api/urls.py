from django.urls import path
from .views import UserCreateAPIView, UserLoginAPIView, UserRegAPI

urlpatterns = [
    path('register', UserCreateAPIView.as_view(), name='register'),
    path('register2', UserRegAPI.as_view(), name='register'),
    path('login', UserLoginAPIView.as_view(), name='login')

]
app_name = 'accounts'