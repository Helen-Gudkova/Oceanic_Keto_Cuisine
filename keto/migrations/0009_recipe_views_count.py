# Generated by Django 4.2 on 2024-05-20 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keto', '0008_recipe_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='views_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]