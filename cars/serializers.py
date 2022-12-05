from rest_framework import serializers
from .models import Car

# We use serializers ensure that all data types are being converted correctly so that it can be interpretted by other programming languages
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'year', 'price']