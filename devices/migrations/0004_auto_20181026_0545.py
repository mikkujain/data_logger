# Generated by Django 2.0.5 on 2018-10-26 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0003_remove_sms_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ports',
            name='port_name',
            field=models.CharField(max_length=5),
        ),
    ]
