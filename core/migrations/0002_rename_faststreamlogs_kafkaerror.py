# Generated by Django 5.0.6 on 2024-05-13 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FastStreamLogs',
            new_name='KafkaError',
        ),
    ]
