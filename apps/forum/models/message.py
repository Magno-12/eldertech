from django.db import models

from apps.base.models.base_model import BaseModel
from apps.users.models.user import User


class Message(BaseModel):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    content = models.TextField()
