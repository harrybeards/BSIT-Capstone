# Generated by Django 3.1.5 on 2021-01-28 01:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('c02e6b4a-aae8-4807-b9c7-c2dfae4b3a9f'), primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(help_text='Title of the meal', max_length=300)),
                ('day', models.DateField(help_text='Day of the week')),
                ('start_time', models.TimeField(blank=True, default=datetime.date.today, help_text='Start time', null=True)),
                ('end_time', models.TimeField(blank=True, help_text='End time', null=True)),
                ('notes', models.TextField(blank=True, help_text='Notes', null=True)),
                ('calendaruser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendar_user.calendaruser')),
            ],
            options={
                'verbose_name': 'Meal',
                'verbose_name_plural': 'Meals',
            },
        ),
    ]