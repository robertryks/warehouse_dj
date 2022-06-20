from django.db import models
from .base_class import BaseClass


class Grade(BaseClass):
    """
    Gatunek stali używany w magazynie
    """
    symbol = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.symbol
