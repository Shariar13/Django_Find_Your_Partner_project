# Generated by Django 3.1.8 on 2022-01-13 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_friend_request'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend_request',
            old_name='friend_username',
            new_name='friend_user_name',
        ),
    ]
