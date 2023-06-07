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

    food_id = serializers.IntegerField(write_only=True)
    price = serializers.IntegerField()
    quantity = serializers.IntegerField(default=0)
    total_price = serializers.IntegerField()
    user_id = serializers.IntegerField(write_only=True)
    # user = UserSerializer(read_only=True)
    # user = user_id = serializers.IntegerField
    class Meta:
        model = Order
        fields = ('food_id', 'price', 'quantity', 'total_price', 'user_id')

    