# Generated by Django 5.0.1 on 2024-02-01 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingrdient',
            new_name='Ingredient',
        ),
    ]
