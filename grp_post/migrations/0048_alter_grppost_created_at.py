# Generated by Django 4.0.2 on 2022-03-10 08:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('grp_post', '0047_alter_grppost_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grppost',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 10, 8, 38, 0, 746723, tzinfo=utc)),
        ),
    ]