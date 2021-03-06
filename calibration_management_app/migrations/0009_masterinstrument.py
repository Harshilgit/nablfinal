# Generated by Django 3.0.6 on 2021-12-22 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calibration_management_app', '0008_auto_20211222_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterInstrument',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('masterinstrument', models.CharField(max_length=200)),
                ('master_serialno', models.CharField(max_length=200, null=True)),
                ('master_idno', models.CharField(max_length=200, null=True)),
                ('range', models.CharField(max_length=200, null=True)),
                ('inservice_date', models.DateField(max_length=100, null=True)),
                ('inservice', models.BooleanField(max_length=100)),
                ('make', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('least_count', models.FloatField(default='', max_length=200)),
                ('resolution', models.FloatField(default='', max_length=200)),
                ('initial_trac', models.CharField(default='', max_length=200)),
                ('acceptance_criteria', models.CharField(default='', max_length=200)),
                ('purchase_from', models.CharField(default='', max_length=200)),
                ('purchase_order', models.CharField(default='', max_length=200)),
                ('purchase_date', models.DateField(max_length=100, null=True)),
                ('date_of_receipt', models.DateField(max_length=100, null=True)),
                ('condition_of_receipt', models.CharField(max_length=200, null=True)),
                ('date_of_inspection', models.DateField(max_length=100, null=True)),
                ('software_details', models.CharField(default='', max_length=200)),
                ('software_idno', models.CharField(default='', max_length=200)),
                ('software_inservice', models.CharField(default='', max_length=200)),
                ('manufacture_instruction', models.CharField(default='', max_length=200)),
                ('national_international_standerd', models.CharField(default='', max_length=200)),
                ('accuracy', models.FloatField(max_length=200, null=True)),
                ('current_inst_condition', models.CharField(max_length=200)),
                ('amount', models.FloatField(max_length=200, null=True)),
                ('parameter_calibrated', models.CharField(max_length=200)),
                ('referance_standard', models.CharField(max_length=200, null=True)),
                ('ext_calibration_agency', models.CharField(max_length=200, null=True)),
                ('cal_frequency', models.CharField(max_length=200)),
                ('certificate_no', models.CharField(max_length=200)),
                ('ulr_no', models.CharField(max_length=200, null=True)),
                ('uncertainity', models.FloatField(blank=True, default=1)),
                ('issue_date', models.DateField(max_length=100)),
                ('exp_date', models.DateField(max_length=100)),
                ('review_of_record', models.BooleanField(max_length=100)),
                ('active_status', models.BooleanField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
