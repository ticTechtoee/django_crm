# Generated by Django 3.2.13 on 2022-08-10 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
