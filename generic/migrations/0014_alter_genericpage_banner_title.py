# Generated by Django 4.0.6 on 2022-07-15 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0013_alter_genericpage_banner_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericpage',
            name='banner_title',
            field=models.TextField(blank=True, default='Welcome to the page about me!', max_length=100),
        ),
    ]
