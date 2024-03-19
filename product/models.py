from django.db import models
from django.utils.translation import gettext_lazy as _


class Car(models.Model):
    class Type(models.IntegerChoices):
        SLOW = 1, _("느림")
        MEDIUM = 2, _("중간")
        FAST = 3, _("빠름")

    name = models.CharField(verbose_name=_("이름"), max_length=100)
    type = models.IntegerField(choices=Type.choices)
