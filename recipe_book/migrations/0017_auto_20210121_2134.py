# Generated by Django 3.1.5 on 2021-01-21 21:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_book', '0016_auto_20210117_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='id',
            field=models.UUIDField(default=uuid.UUID('356938b2-891e-4091-9592-689780d1ac7d'), primary_key=True, serialize=False),
        ),
    ]