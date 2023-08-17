from django.db import models

from apps.base.models.base_model import BaseModel


class InteractiveActivity(BaseModel):
    ACTIVITY_TYPES = [
        ('Exercise', 'Exercise'),
        ('Mental Game', 'Mental Game'),
        ('Socialization', 'Socialization'),
        ('Recreation', 'Recreation'),
        ('Learning', 'Learning')
    ]
    name = models.CharField(max_length=200)
    description = models.TextField()
    activity_type = models.CharField(max_length=100, choices=ACTIVITY_TYPES)
