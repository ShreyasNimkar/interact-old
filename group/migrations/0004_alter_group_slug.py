# Generated by Django 4.0.2 on 2022-02-26 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_groupmembership_alter_group_members_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, unique=True),
        ),
    ]
