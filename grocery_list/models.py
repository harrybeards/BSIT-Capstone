from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import reverse
import uuid


# Create your models here.


class UserGroceryListObject(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_grocerylist(sender, **kwargs):
    """Using a django signal to automatically create model object when user is created"""
    if kwargs.get('created', False):
        UserGroceryListObject.objects.get_or_create(user=kwargs.get('instance'))


class GroceryList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    usergrocerylistobject = models.ForeignKey(UserGroceryListObject, related_name='grocery_list_set', on_delete=models.CASCADE)
    name = models.CharField(max_length=300, help_text='Name of this week\'s grocery list')
    date = models.DateField(help_text='Day to go shopping', blank=True, null=True)
    notes = models.TextField(help_text='Notes about this week\'s list', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('grocery_list:grocery-list-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class GroceryItem(models.Model):
    grocerylist = models.ForeignKey(GroceryList, related_name='grocery_item_set', on_delete=models.CASCADE)
    name = models.CharField(max_length=600, help_text='Name of the grocery Item')
    amount = models.CharField(max_length=20, blank=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
