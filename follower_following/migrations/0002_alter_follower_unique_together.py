# Generated by Django 4.0.2 on 2022-02-26 19:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('follower_following', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follower',
            unique_together={('to_user', 'from_user')},
        ),
    ]