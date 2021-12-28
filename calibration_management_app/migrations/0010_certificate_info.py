# Generated by Django 3.0.6 on 2021-12-23 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calibration_management_app', '0009_masterinstrument'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cert_no', models.CharField(max_length=100)),
                ('ulr_no', models.CharField(max_length=100)),
                ('cal_date', models.DateField()),
                ('due_date', models.DateField()),
                ('r1_1', models.CharField(default='0', max_length=256, null=True)),
                ('r1_2', models.CharField(default='0', max_length=256, null=True)),
                ('r1_3', models.CharField(default='0', max_length=256, null=True)),
                ('r1_4', models.CharField(default='0', max_length=256, null=True)),
                ('r1_5', models.CharField(default='0', max_length=256, null=True)),
                ('r1_6', models.CharField(default='0', max_length=256, null=True)),
                ('r1_7', models.CharField(default='0', max_length=256, null=True)),
                ('r1_8', models.CharField(default='0', max_length=256, null=True)),
                ('r1_9', models.CharField(default='0', max_length=256, null=True)),
                ('r1_10', models.CharField(default='0', max_length=256, null=True)),
                ('r2_1', models.CharField(default='0', max_length=256, null=True)),
                ('r2_2', models.CharField(default='0', max_length=256, null=True)),
                ('r2_3', models.CharField(default='0', max_length=256, null=True)),
                ('r2_4', models.CharField(default='0', max_length=256, null=True)),
                ('r2_5', models.CharField(default='0', max_length=256, null=True)),
                ('r2_6', models.CharField(default='0', max_length=256, null=True)),
                ('r2_7', models.CharField(default='0', max_length=256, null=True)),
                ('r2_8', models.CharField(default='0', max_length=256, null=True)),
                ('r2_9', models.CharField(default='0', max_length=256, null=True)),
                ('r2_10', models.CharField(default='0', max_length=256, null=True)),
                ('r3_1', models.CharField(default='0', max_length=256, null=True)),
                ('r3_2', models.CharField(default='0', max_length=256, null=True)),
                ('r3_3', models.CharField(default='0', max_length=256, null=True)),
                ('r3_4', models.CharField(default='0', max_length=256, null=True)),
                ('r3_5', models.CharField(default='0', max_length=256, null=True)),
                ('r3_6', models.CharField(default='0', max_length=256, null=True)),
                ('r3_7', models.CharField(default='0', max_length=256, null=True)),
                ('r3_8', models.CharField(default='0', max_length=256, null=True)),
                ('r3_9', models.CharField(default='0', max_length=256, null=True)),
                ('r3_10', models.CharField(default='0', max_length=256, null=True)),
                ('r4_1', models.CharField(default='0', max_length=256, null=True)),
                ('r4_2', models.CharField(default='0', max_length=256, null=True)),
                ('r4_3', models.CharField(default='0', max_length=256, null=True)),
                ('r4_4', models.CharField(default='0', max_length=256, null=True)),
                ('r4_5', models.CharField(default='0', max_length=256, null=True)),
                ('r4_6', models.CharField(default='0', max_length=256, null=True)),
                ('r4_7', models.CharField(default='0', max_length=256, null=True)),
                ('r4_8', models.CharField(default='0', max_length=256, null=True)),
                ('r4_9', models.CharField(default='0', max_length=256, null=True)),
                ('r4_10', models.CharField(default='0', max_length=256, null=True)),
                ('r5_1', models.CharField(default='0', max_length=256, null=True)),
                ('r5_2', models.CharField(default='0', max_length=256, null=True)),
                ('r5_3', models.CharField(default='0', max_length=256, null=True)),
                ('r5_4', models.CharField(default='0', max_length=256, null=True)),
                ('r5_5', models.CharField(default='0', max_length=256, null=True)),
                ('r5_6', models.CharField(default='0', max_length=256, null=True)),
                ('r5_7', models.CharField(default='0', max_length=256, null=True)),
                ('r5_8', models.CharField(default='0', max_length=256, null=True)),
                ('r5_9', models.CharField(default='0', max_length=256, null=True)),
                ('r5_10', models.CharField(default='0', max_length=256, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('inst_job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calibration_management_app.InstrumentInfo')),
            ],
        ),
    ]