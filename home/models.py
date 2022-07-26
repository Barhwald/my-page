from tabnanny import verbose
from django.db import models

from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePage(Page):
    banner_title = models.CharField(
        max_length=100,
        default='Welcome to my homepage!',
        blank=True,
        )
    banner_photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        ImageChooserPanel("banner_photo"),
    ]

    # class Meta:
    #     verbose_name = "My home page"
    