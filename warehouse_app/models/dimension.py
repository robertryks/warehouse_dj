from django.db import models
from .base_class import BaseClass


class Dimension(BaseClass):
    """
        Średnica pręta
    """
    value = models.DecimalField(max_digits=4, decimal_places=1, unique=True, default=0.0)

    def __str__(self):
        return self.value
