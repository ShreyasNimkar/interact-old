# Generated by Django 4.0.2 on 2022-03-01 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_remove_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(blank=True, null=True, to='user.Comment'),
        ),
    ]
