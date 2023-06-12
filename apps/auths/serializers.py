from rest_framework import serializers
from auths.models import Order, CustomUser, Purchase


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

    food_id = serializers.IntegerField(write_only=True)
    price = serializers.IntegerField()
    quantity = serializers.IntegerField(default=0)
    total_price = serializers.IntegerField()
    user_id = serializers.IntegerField(write_only=True)
    is_done = serializers.BooleanField()

    class Meta:
        model = Order
        fields = ('food_id', 'price', 'quantity', 'total_price', 'user_id')


class PurchaseSerializer(serializers.ModelSerializer):
    """
    Purchase serializer.
    """

    class Meta:
        model = Purchase
        fields = '__all__'
