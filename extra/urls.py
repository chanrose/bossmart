from django.urls import path
from . import views 

app_name = 'extra'

urlpatterns = [
    path('', views.Voucher.as_view(), name="redeemable_voucher"),
]
