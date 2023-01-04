# Generated by Django 4.1 on 2022-11-18 06:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_foodrequest_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_ondrive',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='foodrequest',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 18, 12, 6, 13, 296127)),
        ),
        migrations.AlterField(
            model_name='user',
            name='verification_status',
            field=models.CharField(choices=[('none', 'none'), ('details_filled', 'details_filled'), ('email_verified', 'email_verified'), ('admin_verified', 'admin_verified')], default='none', max_length=255),
        ),
    ]