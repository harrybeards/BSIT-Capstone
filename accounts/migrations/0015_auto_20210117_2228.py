# Generated by Django 3.1.5 on 2021-01-17 22:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20210117_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('790b9e2c-b81c-4274-978b-f549cb60f542'), primary_key=True, serialize=False),
        ),
    ]
