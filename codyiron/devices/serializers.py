from rest_framework import serializers
from .models import Lamp


class LampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lamp
        fields = ['id', 'name', 'status', 'color', 'brightness']
        read_only = True


lamp_list = [
    {
        'id': 1,
        'name': 'Badezimmer',
        'status': True,
        'color': '#ffffff',
        'brightness': 30
    },
    {
        'id': 4,
        'name': 'Wohnzimmer',
        'status': True,
        'color': '#ffffff',
        'brightness': 65
    },
]
