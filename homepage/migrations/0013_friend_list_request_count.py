# Generated by Django 3.1.8 on 2022-01-14 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_friend_request_request_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend_list',
            name='request_count',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
