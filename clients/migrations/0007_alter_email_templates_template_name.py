# Generated by Django 3.2.13 on 2022-07-24 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_email_templates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_templates',
            name='template_name',
            field=models.CharField(choices=[('TEMP 1', 'Template 1'), ('TEMP 2', 'Template 2')], max_length=50),
        ),
    ]