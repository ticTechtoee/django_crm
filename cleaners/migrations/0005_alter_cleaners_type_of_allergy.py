# Generated by Django 3.2.13 on 2022-07-02 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleaners', '0004_auto_20220702_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleaners',
            name='type_of_allergy',
            field=models.CharField(default='None', max_length=12),
        ),
    ]