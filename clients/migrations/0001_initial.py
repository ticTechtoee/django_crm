# Generated by Django 3.2.13 on 2022-07-26 16:12

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cleaners', '0006_rename_post_code_cleaners_zip_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='email_templates',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('template_name', models.CharField(choices=[('TEMP 1', 'Template 1'), ('TEMP 2', 'Template 2')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='sent_emails',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('email_subject', models.CharField(max_length=50)),
                ('email_body', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('abber_of_notes', models.CharField(default='tba', max_length=4)),
                ('full_form', models.CharField(default='to be allocated', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='zipCode',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('zip_code', models.CharField(blank=True, default='0', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='clients',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('address_line_1', models.CharField(max_length=30)),
                ('address_line_2', models.CharField(max_length=30)),
                ('address_line_3', models.CharField(max_length=30)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='images/profile_images/')),
                ('landline_number', models.CharField(blank=True, max_length=11, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=11, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('date_added', models.DateTimeField()),
                ('preferred_day', models.CharField(choices=[('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), ('THU', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday'), ('SUN', 'Sunday')], max_length=8)),
                ('type', models.CharField(choices=[('RE', 'Regular'), ('O-F', 'One Off')], max_length=6)),
                ('frequency', models.CharField(choices=[('1', 'Weekly'), ('2', 'Monthly'), ('3', 'Fortnightly')], max_length=10)),
                ('number_of_hours', models.IntegerField()),
                ('paying', models.CharField(choices=[('1', 'Yes'), ('2', 'No')], max_length=3)),
                ('paying_methods', models.CharField(choices=[('1', 'DD'), ('2', 'Standing Order(SO)'), ('3', 'Card')], max_length=13)),
                ('ex_cleaners', models.CharField(max_length=20)),
                ('payment_reference', models.CharField(max_length=40)),
                ('cleaner_allocated', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cleaners.cleaners')),
                ('email_to_client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.sent_emails')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.status')),
                ('zip_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.zipcode')),
            ],
        ),
    ]
