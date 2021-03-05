# Generated by Django 3.1.5 on 2021-03-05 20:15

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
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(help_text='Title of the meal', max_length=300)),
                ('date', models.DateTimeField(help_text='Day of the week')),
                ('notes', models.TextField(blank=True, help_text='Notes', null=True)),
                ('calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendar.calendaruser')),
            ],
            options={
                'verbose_name': 'Meal',
                'verbose_name_plural': 'Meals',
            },
        ),
        migrations.CreateModel(
            name='Side',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side', models.CharField(help_text="The Side you'd like to add to the meal", max_length=150)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='side_set', to='calendar.meal')),
            ],
        ),
    ]