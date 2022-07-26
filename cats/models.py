from django.db import models
from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


# Create your models here.

class CatsPage(Page):
    banner_title = models.CharField(
        max_length=100,
        default="It's gonna be 'bout my cats",
        blank=True,
    )

    click_title = models.CharField(
        max_length=100,
        blank=True,
    )

    cat1_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    cat2_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    cat3_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    cat4_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("click_title"),
        ImageChooserPanel("cat1_image"),
        ImageChooserPanel("cat2_image"),
        ImageChooserPanel("cat3_image"),
        ImageChooserPanel("cat4_image"),
    ]