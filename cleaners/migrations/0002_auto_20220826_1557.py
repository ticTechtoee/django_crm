# Generated by Django 3.2.13 on 2022-08-26 10:57

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cleaners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email_add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_add', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='email_content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_subject', models.CharField(max_length=50)),
                ('email_body', ckeditor.fields.RichTextField(blank=True, default='None')),
                ('email_add', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cleaners.email_add')),
            ],
        ),
        migrations.DeleteModel(
            name='sent_emails',
        ),
    ]