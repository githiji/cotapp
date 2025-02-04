from django import forms


class StockForm(forms.Form):
    name = forms.CharField(
       label="Stock Name", max_length=100
    )
    check = forms.BooleanField(
       label="Check", required=False
    )

    