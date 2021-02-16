# Generated by Django 3.1.5 on 2021-01-29 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cook_time',
            field=models.CharField(blank=True, default=0, help_text='The cooking time', max_length=50),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prep_time',
            field=models.CharField(blank=True, default=0, help_text='The preparation time', max_length=50),
        ),
    ]