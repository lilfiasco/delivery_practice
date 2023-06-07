from rest_framework import serializers
from auths.models import Order, CustomUser


class UserSerializer(serializers.ModelSerializer):
    """
    CustomUser serializer.
    """

    class Meta:
        model = CustomUser
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    """
    Order serializer.
    """

    food = serializers.PrimaryKeyRelatedField(read_only=True)
    price = serializers.IntegerField()
    quantity = serializers.IntegerField(default=0)
    total_price = serializers.IntegerField()
    customer = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('food', 'price', 'quantity', 'total_price', 'customer')

    