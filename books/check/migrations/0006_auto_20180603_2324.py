# Generated by Django 2.0.5 on 2018-06-03 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0005_auto_20180603_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlog',
            name='log_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]