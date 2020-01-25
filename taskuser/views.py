from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, LogInSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from rest_framework import permissions,request
from rest_framework.permissions import IsAuthenticated

class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class LogInView(TokenObtainPairView):
    serializer_class = LogInSerializer