# Generated by Django 3.2.13 on 2022-10-17 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleaners', '0003_alter_cleaners_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleaners',
            name='notes',
            field=models.TextField(),
        ),
    ]
