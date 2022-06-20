from django.contrib import admin
from .models.grade import Grade
from .models.dimension import Dimension
from .models.bar import Bar


# Register your models here.
admin.site.register([Grade, Dimension, Bar])
