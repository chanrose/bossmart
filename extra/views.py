from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from oscar.core.loading import get_class, get_model
from django.utils.translation import gettext_lazy as _
from account.models import Account
from django.contrib import messages

# Select three (3) classes that have relationships (association, composition, aggregation, etc.) and belong to different tiers; one class in one tier.
# Select the three (3) most complex functions in each class of the previous point that are related across classes. For measuring the complexity, use cyclomatic complexity. In total, you should come up with nine (9) functions, three (3) per class.
#  Perform unit test on the nine (9) functions. (actually, for upper tiers, unit tests will behave as integration tests)

# Class VoucherView : (View Tier)
## 1. List of available voucher -> Dealing with Visual
## 2. Redeem voucher and whether it save  -> Dealing with Model Manager and Storage
## 3. Redeem voucher without balance

# Class Account 
## 1. Create account ??

PageTitleMixin = get_class('customer.mixins', 'PageTitleMixin')
Voucher = get_model('voucher', 'Voucher')


# Create your views here.
class Voucher(LoginRequiredMixin, PageTitleMixin, generic.ListView):
    model = Voucher
    context_object_name = active_tab = "voucher"
    login_url = '/accounts/login/'
    template_name = 'extra/customer_voucher.html'

    def get(self, request):
        # Show list of available vouchers to redeem and what current user
        # have redeemed
        acc = Account.objects.filter(user=request.user)
        all_vouchers = self.model.objects.all()
        vouchers = []
        for voucher in all_vouchers:
            if not len(voucher.owned_account.all()):
                vouchers.append(voucher)
        if len(acc):
            acc = acc[0]
        else:
            acc = Account.objects.create(user=request.user, balance=0, storage={})
            acc.save()
        context = {
            'page_title': 'Voucher', 
            'active_tab': 'voucher', 
            'Vouchers': vouchers,
            'balance': acc.balance,
            'Owned': acc.vouchers.all()
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        # Send a redeem voucher request
        # Require user to have enough balance
        voucher = self.model.objects.get(pk=request.POST["voucher"])
        voucher_cost = voucher.offers.first().benefit.value + 1000
        acc = Account.objects.get(user=request.user)
        print("Balance", acc.balance, "voucher", voucher_cost)
        if acc.balance >= voucher_cost:
            print("Purchasing...")
            acc.balance -= float(voucher_cost)
            acc.vouchers.add(voucher)
            acc.save()
            messages.success(request, "You have redeem voucher successfully!")
        else:
            messages.info(request, "Sorry, your balance is not enough to redeem")
        return redirect("extra:redeemable_voucher")

def claim_points(req):
    # Check user's order history to see if the order status is shipped yet
    # If the order status is shipped, user get reward in term of 5% of
    # the purchase, and then order status changed to rewarded, so it won't reward 
    # more than one
    acc = Account.objects.get(user=req.user)
    orders = acc.user.orders.all()
    for order in orders:
        if order.status == "Shipped":
            print("Order", order, "Status", order.status)
            order.status = "Rewarded"
            reward = float(order.total_excl_tax)*0.05
            if order.currency == "฿":
                reward = float(order.total_excl_tax)/30 * 0.05
            acc.balance += reward
            order.save()
            messages.success(req, f"You have rewarded {reward:.2f} pts ")
    acc.save()
    return redirect("extra:redeemable_voucher")
