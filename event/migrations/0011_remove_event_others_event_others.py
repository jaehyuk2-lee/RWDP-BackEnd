# Generated by Django 5.1.4 on 2025-01-12 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_remove_event_others_event_others'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='others',
        ),
        migrations.AddField(
            model_name='event',
            name='others',
            field=models.ManyToManyField(blank=True, to='event.etc'),
        ),
    ]
