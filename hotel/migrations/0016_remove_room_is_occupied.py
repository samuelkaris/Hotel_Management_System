# Generated by Django 4.2.1 on 2023-05-20 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0015_room_is_occupied'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='is_occupied',
        ),
    ]
