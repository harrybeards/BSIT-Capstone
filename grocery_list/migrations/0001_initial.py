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
            name='UserGroceryListObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroceryList',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text="Name of this week's grocery list", max_length=300)),
                ('date', models.DateField(blank=True, help_text='Day to go shopping', null=True)),
                ('notes', models.TextField(blank=True, help_text="Notes about this week's list", null=True)),
                ('usergrocerylistobject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grocery_list_set', to='grocery_list.usergrocerylistobject')),
            ],
        ),
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the grocery Item', max_length=600)),
                ('amount', models.CharField(blank=True, max_length=20)),
                ('url', models.URLField(blank=True, null=True)),
                ('grocerylist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grocery_item_set', to='grocery_list.grocerylist')),
            ],
        ),
    ]
