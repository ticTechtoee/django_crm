# Generated by Django 3.2.13 on 2022-07-17 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cleaners', '0005_alter_cleaners_type_of_allergy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cleaners',
            old_name='post_code',
            new_name='zip_code',
        ),
    ]
