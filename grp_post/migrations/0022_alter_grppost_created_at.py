# Generated by Django 4.0.2 on 2022-02-28 03:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('grp_post', '0021_alter_grppost_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grppost',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 28, 3, 2, 28, 448017, tzinfo=utc)),
        ),
    ]
