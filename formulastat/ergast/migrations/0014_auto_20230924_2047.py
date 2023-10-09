# Generated by Django 3.2.21 on 2023-09-24 20:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ergast", "0013_alter_drivers_code"),
    ]

    operations = [
        migrations.AddField(
            model_name="races",
            name="fp1_date",
            field=models.DateField(blank=True, null=True, verbose_name="FP1 date"),
        ),
        migrations.AddField(
            model_name="races",
            name="fp1_time",
            field=models.TimeField(blank=True, null=True, verbose_name="FP1 start time"),
        ),
        migrations.AddField(
            model_name="races",
            name="fp2_date",
            field=models.DateField(blank=True, null=True, verbose_name="FP2 date"),
        ),
        migrations.AddField(
            model_name="races",
            name="fp2_time",
            field=models.TimeField(blank=True, null=True, verbose_name="FP2 start time"),
        ),
        migrations.AddField(
            model_name="races",
            name="fp3_date",
            field=models.DateField(blank=True, null=True, verbose_name="FP3 date"),
        ),
        migrations.AddField(
            model_name="races",
            name="fp3_time",
            field=models.TimeField(blank=True, null=True, verbose_name="FP3 start time"),
        ),
        migrations.AddField(
            model_name="races",
            name="quali_date",
            field=models.DateField(blank=True, null=True, verbose_name="Qualifying date"),
        ),
        migrations.AddField(
            model_name="races",
            name="quali_time",
            field=models.TimeField(blank=True, null=True, verbose_name="Qualifying start time"),
        ),
        migrations.AddField(
            model_name="races",
            name="sprint_date",
            field=models.DateField(blank=True, null=True, verbose_name="Sprint date"),
        ),
        migrations.AddField(
            model_name="races",
            name="sprint_time",
            field=models.TimeField(blank=True, null=True, verbose_name="Sprint start time"),
        ),
    ]
