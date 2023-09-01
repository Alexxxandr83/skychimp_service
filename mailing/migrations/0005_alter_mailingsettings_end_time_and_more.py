# Generated by Django 4.2.4 on 2023-08-20 19:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0004_alter_mailinglog_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingsettings',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 27, 19, 44, 35, 953297, tzinfo=datetime.timezone.utc), null=True, verbose_name='Время окончания'),
        ),
        migrations.AlterField(
            model_name='mailingsettings',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 20, 19, 44, 35, 953274, tzinfo=datetime.timezone.utc), null=True, verbose_name='Время старта'),
        ),
    ]
