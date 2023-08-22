from django import forms

class CuttingForm(forms.Form):
    stock_width = forms.IntegerField(min_value=1, label='Stock Width')
    orders = forms.CharField(label='Orders', widget=forms.TextInput(attrs={'placeholder': 'e.g. 110*5, 120*3'}))

    def clean_orders(self):
        data = self.cleaned_data['orders']
        pairs = data.split(',')
        for pair in pairs:
            try:
                width, quantity = pair.split('*')
                int(width)
                int(quantity)
            except ValueError:
                raise forms.ValidationError("Each order should be in the format 'width*quantity' separated by commas.")

        return data
