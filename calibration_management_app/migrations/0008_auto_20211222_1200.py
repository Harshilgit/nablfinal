# Generated by Django 3.0.6 on 2021-12-22 06:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calibration_management_app', '0007_todo_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='now',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, editable=False),
        ),
    ]
