# Generated by Django 5.0.1 on 2024-02-11 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_mailing_client_mailing_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='client',
            field=models.ManyToManyField(to='main.client', verbose_name='клиент'),
        ),
    ]
