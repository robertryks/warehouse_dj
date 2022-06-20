from rest_framework import serializers
from ..models import Delivery


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['id', 'wz_number', 'delivery_date']
