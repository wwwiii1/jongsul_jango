# Generated by Django 2.0.5 on 2018-06-02 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0003_auto_20180603_0143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlog',
            old_name='user',
            new_name='username',
        ),
    ]