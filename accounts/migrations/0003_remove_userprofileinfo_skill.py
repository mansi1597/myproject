# Generated by Django 2.0.6 on 2018-07-04 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180702_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='skill',
        ),
    ]
