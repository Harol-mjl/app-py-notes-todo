from django.db import models
from django.utils.translation import gettext_lazy as _

class Role(models.TextChoices):
    ADMIN = 'ADMIN', _('Admin')
    EDITOR = 'EDITOR', _('Editor')
    SUPERUSER = 'SUPERUSER', _('Superuser')
    STAFF = 'STAFF', _('Staff')
    GUEST = 'GUEST', _('Guest')
