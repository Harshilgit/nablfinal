# Generated by Django 3.0.6 on 2021-12-24 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calibration_management_app', '0016_auto_20211224_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalcert',
            name='qr_code',
            field=models.ImageField(blank=True, editable=False, upload_to='media/qr_codes'),
        ),
    ]