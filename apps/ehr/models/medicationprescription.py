from django.db import models

from apps.base.models.base_model import BaseModel
from apps.ehr.models.medication import Medication
from apps.users.models.patient import Patient


class MedicationPrescription(BaseModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    request_date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    dose = models.TextField()
    instructions = models.TextField()
