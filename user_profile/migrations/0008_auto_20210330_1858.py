# Generated by Django 3.1.7 on 2021-03-30 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0007_auto_20210330_1828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userarticle',
            old_name='author',
            new_name='user',
        ),
    ]
