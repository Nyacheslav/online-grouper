# Generated by Django 3.0.5 on 2020-05-02 23:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('online_grouper', '0007_auto_20200503_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 5, 2, 23, 32, 24, 314865, tzinfo=utc), verbose_name='Дата измерения'),
        ),
    ]