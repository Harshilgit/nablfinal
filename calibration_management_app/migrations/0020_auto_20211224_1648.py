# Generated by Django 3.0.6 on 2021-12-24 11:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('calibration_management_app', '0019_auto_20211224_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='now',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 24, 11, 18, 58, 964451, tzinfo=utc)),
        ),
    ]
