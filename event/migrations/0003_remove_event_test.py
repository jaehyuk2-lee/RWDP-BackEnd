# Generated by Django 5.1.4 on 2025-01-10 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_event_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='test',
        ),
    ]
