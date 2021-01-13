from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class GroceryList(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class GroceryListWeek(models.Model):
    grocerylist = models.ForeignKey(GroceryList, on_delete=models.CASCADE)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_grocerylist(sender, **kwargs):
    """Using a django signal to automatically create model object when user is created"""
    if kwargs.get('created', False):
        GroceryList.objects.get_or_create(user=kwargs.get('instance'))
