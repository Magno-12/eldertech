from django.db import models

from apps.base.models.base_model import BaseModel


class Forum(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
