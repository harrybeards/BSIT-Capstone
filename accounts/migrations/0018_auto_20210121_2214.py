# Generated by Django 3.1.5 on 2021-01-21 22:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20210121_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5cd88a14-1f58-4e62-8222-43143bb2f91e'), primary_key=True, serialize=False),
        ),
    ]
