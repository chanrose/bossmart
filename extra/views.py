from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from oscar.core.loading import get_class, get_model
from django.utils.translation import gettext_lazy as _
from account.models import Account

PageTitleMixin = get_class('customer.mixins', 'PageTitleMixin')
Voucher = get_model('voucher', 'Voucher')


# Create your views here.
class Voucher(LoginRequiredMixin, PageTitleMixin, generic.ListView):
    model = Voucher
    context_object_name = active_tab = "voucher"
    login_url = '/accounts/login/'
    template_name = 'extra/customer_voucher.html'

    def get(self, request):
        acc = Account.objects.filter(user=request.user)
        if len(acc):
            acc = acc[0]
        else:
            acc = Account.objects.create(user=request.user, balance=0, storage={})
            acc.save()
        context = {
            'page_title': 'Voucher', 
            'active_tab': 'voucher', 
            'Vouchers': self.model.objects.all(),
            'balance': acc.balance
        }
        return render(request, self.template_name, context)

def save_voucher(req, code):
    print("test")