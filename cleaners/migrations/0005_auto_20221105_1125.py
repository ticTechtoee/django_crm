# Generated by Django 3.2.13 on 2022-11-05 06:25

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cleaners', '0004_alter_cleaners_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailsSentToCleaners',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('email_subject', models.CharField(max_length=50)),
                ('email_content', ckeditor.fields.RichTextField(blank=True, default='None')),
                ('email_recipient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cleaners.cleaners')),
            ],
        ),
        migrations.RemoveField(
            model_name='email_content',
            name='email_add',
        ),
        migrations.DeleteModel(
            name='Email_add',
        ),
        migrations.DeleteModel(
            name='email_content',
        ),
    ]
