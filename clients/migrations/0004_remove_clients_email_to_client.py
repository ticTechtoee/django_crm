# Generated by Django 3.2.13 on 2022-06-30 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20220630_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='email_to_client',
        ),
    ]
