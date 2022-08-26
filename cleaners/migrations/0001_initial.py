# Generated by Django 3.2.13 on 2022-08-26 09:57

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sent_emails',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('receiving_end', models.EmailField(max_length=254)),
                ('email_subject', models.CharField(max_length=50)),
                ('email_body', ckeditor.fields.RichTextField(blank=True, default='None')),
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
            name='cleaners',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('address_line1', models.CharField(max_length=30)),
                ('address_line2', models.CharField(max_length=30)),
                ('address_line3', models.CharField(max_length=30)),
                ('zip_code', models.CharField(max_length=6)),
                ('landline_number', models.CharField(max_length=11)),
                ('mobile_number', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('date_added', models.DateField()),
                ('number_of_hours_wanted', models.IntegerField()),
                ('nationality', models.CharField(max_length=20)),
                ('permit_to_work_needed', models.CharField(choices=[('1', 'Yes'), ('2', 'No')], max_length=3)),
                ('emergency_contact_number', models.CharField(max_length=11)),
                ('emergency_contact_name', models.CharField(max_length=11)),
                ('relationship_to_emergency_contact', models.CharField(max_length=10)),
                ('Disclouser', models.CharField(choices=[('1', 'Yes'), ('2', 'No')], max_length=3)),
                ('NI_Nunber', models.CharField(max_length=9)),
                ('consent_for_DBS', models.CharField(choices=[('1', 'Yes'), ('2', 'No')], max_length=3)),
                ('smoker', models.CharField(choices=[('1', 'Yes'), ('2', 'No')], max_length=3)),
                ('can_iron', models.CharField(choices=[('1', 'Yes'), ('2', 'No')], max_length=3)),
                ('driver', models.CharField(choices=[('1', 'Yes'), ('2', 'No')], max_length=3)),
                ('has_car', models.CharField(choices=[('1', 'Yes'), ('2', 'No')], max_length=3)),
                ('referee_1_details', models.CharField(max_length=50)),
                ('referee_2_details', models.CharField(max_length=50)),
                ('areas_worked', models.CharField(max_length=50)),
                ('prev_work_experience', models.CharField(max_length=30)),
                ('prev_convicted_of_offence', models.CharField(choices=[('1', 'Yes'), ('2', 'No')], max_length=3)),
                ('pet_allergies', models.CharField(choices=[('1', 'Yes'), ('2', 'No')], max_length=3)),
                ('type_of_allergy', models.CharField(default='None', max_length=12)),
                ('transactions_date', models.DateField()),
                ('valid_cleaner', models.CharField(blank=True, choices=[('1', 'Yes'), ('2', 'No')], max_length=3)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cleaners.status')),
            ],
        ),
    ]
