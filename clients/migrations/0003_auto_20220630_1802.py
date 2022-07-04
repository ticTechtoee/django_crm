# Generated by Django 3.2.13 on 2022-06-30 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20220630_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='contact_number',
        ),
        migrations.AddField(
            model_name='clients',
            name='landline_number',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.DeleteModel(
            name='contact_number',
        ),
    ]