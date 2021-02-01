from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import reverse
from django.core.exceptions import ValidationError
import uuid, datetime

# Create your models here.


class CalendarUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_calendar(sender, **kwargs):
    """Using a django signal to automatically create model object when user is created"""
    if kwargs.get('created', False):
        CalendarUser.objects.get_or_create(user=kwargs.get('instance'))


class Meal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    calendaruser = models.ForeignKey(CalendarUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, help_text='Title of the meal', unique=False)
    day = models.DateField(help_text='Day of the week', unique=False)
    start_time = models.TimeField(help_text='Start time', blank=True, null=True)
    end_time = models.TimeField(help_text='End time', blank=True, null=True)
    notes = models.TextField(help_text='Notes', blank=True, null=True)

    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:    # edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) \
            or (new_end >= fixed_start and new_end <= fixed_end): # inner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end: # outer limits
            overlap = True
        return overlap

    def clean(self):
        # Checking to make sure that if the fields are empty, we don't try to run validation on them
        if self.start_time and self.end_time is not None:
            if self.end_time <= self.start_time:
                raise ValidationError('Ending times must be after starting times')

        meals = Meal.objects.filter(day=self.day)
        if meals.exists():
            for meal in meals:
                if self.start_time and self.end_time is not None:
                    if self.check_overlap(meal.start_time, meal.end_time, self.start_time, self.end_time):
                        raise ValidationError(
                            'There is an overlap with another meal: ' + str(meal.day) + ',' + str(
                                meal.start_time) + '-' + str(meal.end_time))

    def get_absolute_url(self):
        return reverse('calendar_user:meal-detail', args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Meal'
        verbose_name_plural = 'Meals'

