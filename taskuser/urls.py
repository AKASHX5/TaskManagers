from django.urls import path,include
from .views import SignUpView, LogInView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('api/v1/sign_up/', SignUpView.as_view(), name = 'sign_up'),
    path('log_in/', LogInView.as_view(), name = 'log_in'),

    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    ]

