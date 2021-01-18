from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import reverse
import uuid
# Create your models here.


class RecipeBook(models.Model):
    """Each user has a single associated RecipeBook object, linked in this OneToOne field"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_recipebook(sender, **kwargs):
    """Using a django signal to automatically create model object when user is created"""
    if kwargs.get('created', False):
        RecipeBook.objects.get_or_create(user=kwargs.get('instance'))


class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    recipebook = models.ForeignKey(RecipeBook, related_name='recipe_set', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, help_text='Title of the recipe')
    description = models.TextField(help_text='Description of the recipe', blank=True)
    # image = models.ImageField(height_field=, width_field=, help_text='Image of the recipe', blank=True)
    servings = models.PositiveSmallIntegerField(help_text='The amount of servings the recipe will yield', default=0, blank=True)
    prep_time = models.PositiveSmallIntegerField(help_text='The preparation time', default=0, blank=True)
    cook_time = models.PositiveSmallIntegerField(help_text='The cooking time', default=0, blank=True)
    url = models.URLField(blank=True)

    TIME_UNITS = (
        ('m', 'Minutes'),
        ('h', 'Hours')
    )

    def get_absolute_url(self):
        return reverse('recipe_book:recipe-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredient_set', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Direction(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='direction_set', on_delete=models.CASCADE)
    step_instructions = models.TextField(help_text='Write the instructions of the step here')
