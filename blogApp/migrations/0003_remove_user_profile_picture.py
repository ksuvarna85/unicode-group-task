# Generated by Django 3.0.3 on 2020-10-31 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_auto_20201031_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_picture',
        ),
    ]