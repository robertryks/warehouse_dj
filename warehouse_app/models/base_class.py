import datetime

from django.db import models


class BaseClass(models.Model):
    """
        Klasa bazowa dla wszystkich modeli, ustawiająca pola created_at i updated_at
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
