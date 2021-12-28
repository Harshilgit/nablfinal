# Generated by Django 3.0.6 on 2021-12-22 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calibration_management_app', '0004_todo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='assigned_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calibration_management_app.LoggedInUser'),
        ),
    ]
