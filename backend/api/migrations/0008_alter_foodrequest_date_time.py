# Generated by Django 4.1 on 2022-11-06 05:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_foodrequest_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodrequest',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 6, 10, 49, 55, 188238)),
        ),
    ]
