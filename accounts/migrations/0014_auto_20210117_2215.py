# Generated by Django 3.1.5 on 2021-01-17 22:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20210117_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8cc2f3b7-a469-4620-8a58-a211169f9c3a'), primary_key=True, serialize=False),
        ),
    ]