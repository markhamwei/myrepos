# Generated by Django 4.2 on 2023-05-21 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_questionresponse_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionresponse',
            old_name='response_time',
            new_name='response_datetime',
        ),
    ]
