# Generated by Django 4.0.2 on 2022-03-01 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_alter_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
    ]
