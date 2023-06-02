from rest_framework import serializers
from .models import Food


class FoodSerializer(serializers.ModelSerializer):
    """
    Food serializer for cart.
    """

    class Meta:
        model = Food
        fields = '__all__'
