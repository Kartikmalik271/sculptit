# Generated by Django 3.0.5 on 2021-03-30 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_auto_20210330_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userarticle',
            name='user',
        ),
    ]
