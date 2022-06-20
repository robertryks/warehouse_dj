from django.db import models
from .base_class import BaseClass
from .delivery import Delivery


class DeliveryDetails(BaseClass):
    """
    Klasa reprezentująca pozycję dostawy dla wybranej WZ
    """
    heat = models.CharField(max_length=20)
    weight = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    certificate = models.CharField(max_length=30)

    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)

    def __str__(self):
        return "{}*{} - {} kg".format(self.heat, self.certificate, self.weight)
