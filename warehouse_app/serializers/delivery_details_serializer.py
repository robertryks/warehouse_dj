from rest_framework import serializers
from ..models import DeliveryDetails


class DeliveryDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryDetails
        fields = ['id', 'heat', 'weight', 'certyficate', 'delivery']
