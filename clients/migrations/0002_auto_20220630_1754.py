# Generated by Django 3.2.13 on 2022-06-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='type_of_notes',
        ),
        migrations.AddField(
            model_name='status',
            name='abber_of_notes',
            field=models.CharField(default='tba', max_length=4),
        ),
        migrations.AddField(
            model_name='status',
            name='full_form',
            field=models.CharField(default='to be allocated', max_length=30),
        ),
    ]
