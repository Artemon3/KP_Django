# Generated by Django 5.0.1 on 2024-02-08 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_message_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailing',
            name='time_mailing',
        ),
    ]
