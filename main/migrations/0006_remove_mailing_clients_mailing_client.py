# Generated by Django 5.0.1 on 2024-02-08 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_mailing_is_activated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailing',
            name='clients',
        ),
        migrations.AddField(
            model_name='mailing',
            name='client',
            field=models.ManyToManyField(to='main.client', verbose_name='клиент'),
        ),
    ]
