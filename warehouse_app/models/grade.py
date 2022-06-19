from django.db import models


class Grade(models.Model):
    """
    Gatunek stali używany w magazynie
    """
    symbol = models.CharField(max_length=30, blank=False, null=False, unique=True)

    def __str__(self):
        return self.symbol
