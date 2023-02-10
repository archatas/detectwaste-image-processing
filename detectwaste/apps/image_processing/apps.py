from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ImageProcessingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "detectwaste.apps.image_processing"
    verbose_name = _("Image Processing")
