# Generated by Django 3.1.5 on 2021-01-16 23:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210116_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('99952bd6-0b16-4e7a-b577-77ae575155be'), primary_key=True, serialize=False),
        ),
    ]
