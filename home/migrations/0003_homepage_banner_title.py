# Generated by Django 4.0.6 on 2022-07-07 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_title',
            field=models.CharField(default='Welcome to my homepage!', max_length=100),
        ),
    ]