# Generated by Django 5.0.1 on 2024-02-01 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_ingredient_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='reciperequirement',
            name='quantity',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]