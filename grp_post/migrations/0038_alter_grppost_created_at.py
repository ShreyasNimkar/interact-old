# Generated by Django 4.0.2 on 2022-03-02 10:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('grp_post', '0037_alter_grppost_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grppost',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 2, 10, 45, 49, 987027, tzinfo=utc)),
        ),
    ]
