# Generated by Django 3.1.5 on 2021-01-16 21:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210116_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('d7d0d86e-daf5-41bc-a8b4-2e136d242aff'), primary_key=True, serialize=False),
        ),
    ]
