# Generated by Django 4.0.6 on 2022-07-15 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0010_alter_genericpage_banner_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericpage',
            name='banner_title',
            field=models.CharField(default='Welcome to the page about me!', max_length=100, null=True),
        ),
    ]
