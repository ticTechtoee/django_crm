# Generated by Django 3.2.13 on 2022-07-02 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleaners', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cleaners',
            name='address',
        ),
        migrations.AddField(
            model_name='cleaners',
            name='address_line1',
            field=models.CharField(default='None', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cleaners',
            name='address_line2',
            field=models.CharField(default='None', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cleaners',
            name='address_line3',
            field=models.CharField(default='None', max_length=30),
            preserve_default=False,
        ),
    ]
