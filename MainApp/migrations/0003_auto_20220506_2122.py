# Generated by Django 3.2.13 on 2022-05-07 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_rename_pizza_name_pizza_text_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='text',
            new_name='pizza_name',
        ),
        migrations.RenameField(
            model_name='topping',
            old_name='text',
            new_name='toppings_name',
        ),
    ]
