# Generated by Django 3.2.13 on 2022-10-15 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='role',
            field=models.CharField(choices=[('Client', 'Client'), ('Cleaner', 'Cleaner')], max_length=7),
        ),
    ]
