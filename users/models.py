from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class PhoneNumber(models.Model):
    """Docstring for PhoneNumber"""

    phone = models.CharField(
        help_text=_("Número de telefone. Preencha apenas com números."),
        verbose_name=_("Número de Telefone"),
        max_length=15, null=False, blank=False)

    class Meta:
        verbose_name = _('Número de telefone')
        verbose_name_plural = _('Números de telefone')

    def __str__(self):
        return self.phone


class PetUser(User):
    """Docstring for PetUser"""
    phone_numbers = models.ManyToManyField(PhoneNumber)

    class Meta:
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')

    def __str__(self):
        return (self.first_name + " " + self.last_name)
