# Generated by Django 4.0.6 on 2022-07-19 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0002_alter_socialmediasettings_instagram'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmediasettings',
            name='facebook',
            field=models.URLField(blank=True, max_length=100),
        ),
    ]
