from django.db import models

from apps.base.models.base_model import BaseModel
from apps.users.models.user import User
from apps.forum.models.forum import Forum


class ForumComment(BaseModel):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
