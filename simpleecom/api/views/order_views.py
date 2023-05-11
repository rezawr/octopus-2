from rest_framework.generics import CreateAPIView, UpdateAPIView

from simpleecom.api.serializers.order_serializer import OrderSerializer, AcceptOrderSerializer


class CreateOrder(CreateAPIView):
    serializer_class = OrderSerializer
    queryset = OrderSerializer.Meta.model.objects.all()


class AcceptOrder(UpdateAPIView):
    serializer_class = AcceptOrderSerializer
    queryset = AcceptOrderSerializer.Meta.model.objects.all()
