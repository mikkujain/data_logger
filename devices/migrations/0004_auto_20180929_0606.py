# Generated by Django 2.0.5 on 2018-09-29 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0003_auto_20180929_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
