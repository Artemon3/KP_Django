# Generated by Django 5.0.1 on 2024-02-11 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_mailing_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.TextField(max_length=40, verbose_name='Тема письма'),
        ),
    ]