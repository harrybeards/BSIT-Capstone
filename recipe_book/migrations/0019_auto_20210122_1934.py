# Generated by Django 3.1.5 on 2021-01-22 19:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_book', '0018_auto_20210121_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='id',
            field=models.UUIDField(default=uuid.UUID('43c14a71-9e51-4249-88c7-75d3fb47db82'), primary_key=True, serialize=False),
        ),
    ]
