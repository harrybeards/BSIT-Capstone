from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid # To create a unique User ID


# Create your models here.


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    def __str__(self):
        return self.username