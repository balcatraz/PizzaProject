# Generated by Django 4.0.4 on 2022-05-06 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='pizza_name',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='topping',
            old_name='topping_name',
            new_name='text',
        ),
    ]
