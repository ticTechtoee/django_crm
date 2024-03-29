# Generated by Django 3.2.13 on 2022-10-15 07:36

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
            name='Email_add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_add', models.EmailField(max_length=254)),
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
            name='email_content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_subject', models.CharField(max_length=50)),
                ('email_body', ckeditor.fields.RichTextField(blank=True, default='None')),
                ('email_add', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cleaners.email_add')),
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
                ('post_code', models.CharField(default='0', max_length=8)),
                ('landline_number', models.CharField(max_length=11)),
                ('mobile_number', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('date_added', models.DateField()),
                ('number_of_hours_wanted', models.IntegerField()),
                ('nationality', models.CharField(max_length=20)),
                ('permit_to_work_needed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('permit_image', models.ImageField(blank=True, null=True, upload_to='permit_images/')),
                ('emergency_contact_number', models.CharField(max_length=11)),
                ('emergency_contact_name', models.CharField(max_length=11)),
                ('relationship_to_emergency_contact', models.CharField(max_length=10)),
                ('Disclosure', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('NI_Number', models.CharField(max_length=9)),
                ('consent_for_DBS', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('smoker', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('can_iron', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('driver', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('has_car', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('referee_1_details', models.TextField()),
                ('referee_2_details', models.TextField()),
                ('areas_worked', models.CharField(max_length=50)),
                ('prev_work_experience', models.CharField(max_length=30)),
                ('prev_convicted_of_offence', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('pet_allergies', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('type_of_allergy', models.CharField(default='None', max_length=50)),
                ('transactions_date', models.DateField()),
                ('valid_cleaner', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('notes', models.TextField(default='15.10.2022 12:36:13')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cleaners.status')),
            ],
        ),
    ]
