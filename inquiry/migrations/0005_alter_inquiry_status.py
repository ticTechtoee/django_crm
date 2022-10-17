# Generated by Django 3.2.13 on 2022-10-17 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0004_alter_inquiry_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Allocated', 'Allocated')], default='Pending', max_length=9),
        ),
    ]
