# Generated by Django 4.2 on 2023-05-21 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_response_time_questionresponse_response_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionresponse',
            name='response_peeked',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]