from django import forms

from .models import *


class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ('amount',)