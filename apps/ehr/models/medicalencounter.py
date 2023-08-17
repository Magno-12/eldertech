from django.db import models

from apps.base.models.base_model import BaseModel
from apps.users.models.patient import Patient


class MedicalEncounter(BaseModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    encounter_date = models.DateTimeField()
    notes = models.TextField()
    visit_reason = models.TextField()
    diagnosis = models.TextField()
    recommendations = models.TextField()
