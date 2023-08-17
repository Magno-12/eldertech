from django.db import models

from apps.base.models.base_model import BaseModel


class Resource(BaseModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    resource_type = models.CharField(max_length=100,
        choices=[('Article', 'Article'),
            ('Tip', 'Tip'),
            ('Tutorial', 'Tutorial'),
            ('Activity', 'Activity')]
        )
