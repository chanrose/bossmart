from django.db import models
from django.contrib.auth.models import (
    AbstractUser, BaseUserManager, AbstractBaseUser)
from oscar.core.compat import AUTH_USER_MODEL
from oscar.core.loading import get_model
import jsonfield

Voucher = get_model('voucher', 'Voucher')
# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="accountuser")
    balance = models.FloatField()
    storage = jsonfield.JSONField(null=True)
    vouchers = models.ManyToManyField(Voucher, blank=True, related_name="owned_account")


    def __str__(self):
        return f"{self.user}: {self.balance}"

