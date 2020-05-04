# Generated by Django 3.0.5 on 2020-05-02 23:54

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('online_grouper', '0010_auto_20200503_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 5, 2, 23, 54, 21, 344954, tzinfo=utc), verbose_name='Дата измерения'),
        ),
        migrations.AlterField(
            model_name='signal',
            name='file',
            field=models.FileField(upload_to='signals/', validators=[django.core.validators.FileExtensionValidator(['txt'])], verbose_name='Файл'),
        ),
    ]