from django import forms
# from bootstrap_datepicker_plus import DatePickerInput

from django.forms import ModelForm
from .models import *



class PunchForm(forms.ModelForm):
    class Meta:
        model = PunchTable
        # exclude = ('client_product_id',)
        fields = '__all__'
