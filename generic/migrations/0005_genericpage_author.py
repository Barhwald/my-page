# Generated by Django 4.0.6 on 2022-07-08 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0004_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='genericpage',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='generic.author'),
        ),
    ]