from re import template
from django.db import models
from wagtail.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

# Create your models here.
class cat1_display(Page):

    body = StreamField([
        ('name', blocks.CharBlock()),
        ('image', ImageChooserBlock()),
    ], null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]