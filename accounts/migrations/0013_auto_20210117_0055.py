# Generated by Django 3.1.5 on 2021-01-17 00:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20210117_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('7005bd8d-0184-42d2-88f1-e9dd45d7a1f4'), primary_key=True, serialize=False),
        ),
    ]