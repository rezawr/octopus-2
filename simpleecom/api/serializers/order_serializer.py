import uuid

from rest_framework import serializers

from simpleecom.order.models import Order
from simpleecom.order.models import STATUS


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('shipping_code',)


class AcceptOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('status',)

    def update(self, instance, validated_data):
        update = super().update(instance, validated_data)
        if update.status == STATUS.shipping:
            update.shipping_code = uuid.uuid4().hex[:8]
            update.save()

        return update
