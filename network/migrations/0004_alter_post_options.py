# Generated by Django 3.2 on 2022-05-23 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_rename_post_time_post_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-time']},
        ),
    ]
