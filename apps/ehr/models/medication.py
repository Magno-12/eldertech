from django.db import models

from apps.base.models.base_model import BaseModel


class Medication(BaseModel):
    code = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
    manufacturer = models.TextField()
    form = models.TextField()  # Example: pill, liquid, injection.
    quantity = models.IntegerField()
