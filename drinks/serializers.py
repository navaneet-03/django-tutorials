from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializer.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']
