# Generated by Django 4.0.2 on 2022-02-26 11:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='day_added',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 2, 26, 11, 37, 52, 522984, tzinfo=utc)),
        ),
    ]