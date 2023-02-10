import os
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


def upload_to(instance, filename):
    now = timezone.now()
    filename_base, filename_ext = os.path.splitext(filename)
    return "images/{filename}{ext}".format(
        filename=now.strftime("%Y%m%d%H%M%S"),
        ext=filename_ext.lower(),
    )


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    slug = models.SlugField(_("Slug"), max_length=200, unique=True)

    class Meta:
        ordering = ["title"]
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title


class ProcessedImage(models.Model):
    STATUS_IN_PROGRESS = "i"
    STATUS_PROCESSED = "p"
    STATUS_CHOICES = [
        (STATUS_IN_PROGRESS, _("In progress")),
        (STATUS_PROCESSED, _("Processed")),
    ]
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    processed = models.DateTimeField(_("Processed"), blank=True, null=True)
    image = models.ImageField(_("Image"), upload_to=upload_to)
    status = models.CharField(
        _("Status"), max_length=1, choices=STATUS_CHOICES, default=STATUS_IN_PROGRESS
    )
    categories = models.ManyToManyField(
        Category, verbose_name=_("Categories"), blank=True
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Processed Image")
        verbose_name_plural = _("Processed Images")

    def __str__(self):
        return self.image.path

    def get_api_endpoint_url(self):
        return reverse("processed_image_detail", kwargs={"pk": self.pk})
