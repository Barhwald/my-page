# Generated by Django 4.0.6 on 2022-07-19 13:51

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0018_alter_genericpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericpage',
            name='body',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock(template='paragraph_block.html')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.blocks.CharBlock(template='heading_block.html'))], null=True, use_json_field=None),
        ),
    ]
