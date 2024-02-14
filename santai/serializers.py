from rest_framework import serializers

from santai.models import Order, CertificateOrder


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['name', 'phone']


class CertificateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateOrder
        fields = ['name', 'phone', 'massage', 'time']
