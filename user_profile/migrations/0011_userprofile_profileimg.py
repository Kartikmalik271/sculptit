# Generated by Django 3.1.7 on 2021-04-04 09:51

from django.db import migrations, models
import user_profile.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0010_userarticle'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profileimg',
            field=models.ImageField(default='', upload_to=user_profile.models.uplaod_path),
        ),
    ]
