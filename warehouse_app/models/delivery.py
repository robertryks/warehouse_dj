import datetime

from django.db import models
from .base_class import BaseClass

class Delivery(BaseClass):
    """
    Klasa reprezentuje nagłówek dostawy (WZ)
    """
    wz_number = models.CharField(max_length=20, null=False, blank=False, unique=True)
    delivery_date = models.DateField(default=datetime.date.today(), blank=False, null=False)

    def __str__(self):
        return "WZ nr {} z dnia {}".format(self.wz_number, self.delivery_date)
