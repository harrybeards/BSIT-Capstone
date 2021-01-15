# Generated by Django 3.1.5 on 2021-01-15 22:41

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
            name='RecipeBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('5fa2be61-8256-49b1-8cfa-19777ae7c5c6'), primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='Title of the recipe', max_length=150)),
                ('description', models.TextField(blank=True, help_text='Description of the recipe')),
                ('servings', models.PositiveSmallIntegerField(blank=True, default=0, help_text='The amount of servings the recipe will yield')),
                ('prep_time', models.PositiveSmallIntegerField(blank=True, default=0, help_text='The preparation time')),
                ('cook_time', models.PositiveSmallIntegerField(blank=True, default=0, help_text='The cooking time')),
                ('url', models.URLField(blank=True)),
                ('recipebook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_book.recipebook')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_book.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_number', models.SmallIntegerField()),
                ('step_instructions', models.TextField(help_text='Write the instructions of the step here')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_book.recipe')),
            ],
        ),
    ]
