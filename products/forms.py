from django import forms
from .models import GiftVoucher


class GiftVoucherForm(forms.ModelForm):

    class Meta:
        model = GiftVoucher
        fields = ('amount',)
