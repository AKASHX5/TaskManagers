from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.decorators import permission_classes, action
from .serializers import TaskSerializer


User = get_user_model()

# Create your views here.


class IsAnonCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST" and not request.user.is_authenticated:
            return True
        elif not request.user.is_authenticated and request.method != "POST":
            return False
        elif request.method in permissions.SAFE_METHODS:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.username == request.user.username


class TaskView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes((IsAnonCreate,))

    def perform_create(self, serializer):

        created_by = get_list_or_404(User, id=self.request.data.get('User_id'))
        return serializer.save(created_by=created_by)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


