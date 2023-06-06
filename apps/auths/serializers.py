from rest_framework import serializers
from auths.models import Order


class OrderSerializer(serializers.ModelSerializer):
    """
    Order serializer.
    """

    class Meta:
        model = Order
        fields = '__all__'

    