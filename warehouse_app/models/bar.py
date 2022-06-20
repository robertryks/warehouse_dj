from django.db import models
from .base_class import BaseClass
from .grade import Grade
from .dimension import Dimension


class Bar(BaseClass):
    """
    Klasa reprezentująca pręt o określonej średnicy i wytopie na stanie magazynu
    """
    # TODO: ukończyć klasę Bar
    weight = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)

    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.dimension, self.grade)

    class Meta:
        unique_together = [['grade', 'dimension']]
