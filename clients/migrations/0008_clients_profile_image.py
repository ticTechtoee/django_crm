# Generated by Django 3.2.13 on 2022-07-24 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_alter_email_templates_template_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
    ]
