# Generated by Django 4.2.4 on 2023-08-24 18:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0006_client_owner_mailingclient_owner_mailinglog_owner_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailingsettings',
            options={'permissions': [('set_status', 'Can change status')], 'verbose_name': 'Настройка', 'verbose_name_plural': 'Настройки'},
        ),
        migrations.AlterField(
            model_name='mailingsettings',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 31, 18, 42, 29, 706791, tzinfo=datetime.timezone.utc), null=True, verbose_name='Время окончания'),
        ),
        migrations.AlterField(
            model_name='mailingsettings',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 24, 18, 42, 29, 706772, tzinfo=datetime.timezone.utc), null=True, verbose_name='Время старта'),
        ),
    ]