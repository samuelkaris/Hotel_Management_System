# Generated by Django 4.2.1 on 2023-05-23 09:19

from django.db import migrations, models
import reservation.models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_reservation_end_time_reservation_start_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='end_time',
            field=models.TimeField(default=reservation.models.end_time),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='start_time',
            field=models.TimeField(default=reservation.models.start_time),
        ),
    ]