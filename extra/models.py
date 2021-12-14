from django.db import models
from oscar.core.loading import get_model
from oscar.core.compat import AUTH_USER_MODEL

# Create your models here.
Voucher = get_model('voucher', 'Voucher')

# class UsedVoucher(models.Model):
#     jk