# Generated by Django 2.1.2 on 2019-01-26 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cover_pic',
            field=models.ImageField(default='cover_pics/None/cover_default.jpg', upload_to='cover_pics/'),
        ),
    ]
