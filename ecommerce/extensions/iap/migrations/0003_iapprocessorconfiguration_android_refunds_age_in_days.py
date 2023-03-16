# Generated by Django 3.2.15 on 2023-03-13 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iap', '0002_paymentprocessorresponseextension'),
    ]

    operations = [
        migrations.AddField(
            model_name='iapprocessorconfiguration',
            name='android_refunds_age_in_days',
            field=models.PositiveSmallIntegerField(default=3, verbose_name='Past number of days to fetch Android refunds for.'),
        ),
    ]
