from django.db import models

from apps.base.models.base_model import BaseModel
from apps.users.models.patient import Patient


class MedicalRecords(BaseModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField()
    type = models.TextField()  # Example: Blood pressure, glucose level, weight.
    value = models.TextField()
    units = models.CharField(max_length=50)
    comment = models.TextField(blank=True, null=True)
