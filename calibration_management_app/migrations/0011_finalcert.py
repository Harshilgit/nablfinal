# Generated by Django 3.0.6 on 2021-12-23 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calibration_management_app', '0010_certificate_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finalcert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cert_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='calibration_management_app.Certificate_info')),
                ('inst_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calibration_management_app.InstrumentInfo')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calibration_management_app.MasterInstrument')),
            ],
        ),
    ]
