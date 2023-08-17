from django.db import models

from apps.base.models.base_model import BaseModel
from apps.users.models.user import User


class Patient(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=200, unique=True, db_index=True)
    active = models.BooleanField(default=True)
    family_name = models.CharField(max_length=200)
    given_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    suffix = models.CharField(max_length=20, blank=True, null=True)
    prefix = models.CharField(max_length=20, blank=True, null=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(
        max_length=50,
        db_index=True,
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other'),
            ('Unknown', 'Unknown')
        ]
    )
    birth_date = models.DateField()
    address = models.TextField()
    marital_status = models.CharField(
        max_length=50,
        choices=[
            ('Single', 'Single'),
            ('Married', 'Married'),
            ('Divorced', 'Divorced'),
            ('Widowed', 'Widowed')
        ],
        blank=True, 
        null=True,
        db_index=True
    )
    photo = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)  # Language spoken by the patient

    @property
    def email(self):
        return self.user.email
