# Generated by Django 3.2.13 on 2022-09-19 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleaners', '0006_auto_20220919_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='cleaners',
            name='notes',
            field=models.TextField(default='None'),
        ),
    ]