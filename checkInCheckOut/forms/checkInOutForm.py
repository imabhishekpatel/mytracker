# forms.py

from django import forms

class CheckInOutForm(forms.Form):
    action = forms.CharField(max_length=10)
