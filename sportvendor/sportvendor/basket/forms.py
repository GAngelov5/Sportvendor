from django import forms
from django.core.validators import RegexValidator


class CreditCardForm(forms.Form):
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)
    cardholders_name = forms.CharField(max_length=35)
    month = forms.IntegerField(validators=[RegexValidator(r'^\d{1,2}$')])
    year = forms.IntegerField(validators=[RegexValidator(r'^\d{4}$')])
    number = forms.CharField(validators=[RegexValidator(r'^\d{13}$')])
    verify_val = forms.CharField(validators=[RegexValidator(r'^\d{3}$')])
