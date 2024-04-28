# Generated by Django 4.2 on 2024-04-10 21:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('keto', '0005_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='meal_time',
            field=models.CharField(choices=[('Breakfast', 'Завтрак'), ('Lunch', 'Обед'), ('Dinner', 'Ужин'), ('Snack', 'Перекус')], default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]