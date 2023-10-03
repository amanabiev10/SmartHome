from rest_framework import serializers
from .models import Lamp


class LampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lamp
        fields = ['id', 'name', 'status', 'color', 'brightness']
        read_only = True
