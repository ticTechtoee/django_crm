# Generated by Django 3.2.13 on 2022-09-19 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='clients',
            name='post_code',
            field=models.CharField(default='0', max_length=8),
        ),
    ]