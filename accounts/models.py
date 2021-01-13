from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid # To create a unique User ID
from django.dispatch import receiver
from django.db.models.signals import post_save
from calendar.models import Calendar
from recipe_book.models import RecipeBook
from grocery_list.models import GroceryList


# Create your models here.


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())

    def __str__(self):
        return self.username