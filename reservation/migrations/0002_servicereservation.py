# Generated by Django 4.2.1 on 2023-05-19 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0012_service'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_date', models.DateField()),
                ('reservation_time', models.TimeField()),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.service')),
            ],
        ),
    ]