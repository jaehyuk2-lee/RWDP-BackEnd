# Generated by Django 5.1.4 on 2025-01-12 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_alter_event_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='others',
            field=models.ManyToManyField(null=True, to='event.etc'),
        ),
    ]
