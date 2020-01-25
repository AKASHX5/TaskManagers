from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Task
from taskuser.serializers import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()
    assigned_to = UserSerializer(many=True)

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        return Task.objects.create(**validated_data)