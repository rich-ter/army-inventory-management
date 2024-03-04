from django import forms
from .models import Product, Shipment

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg bg-inverse bg-opacity-5', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg bg-inverse bg-opacity-5', 'placeholder': 'Password'})
    )


class ProductForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Onoma'}))
    serial_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seiriakos'}), required=False)
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'summernote', 'rows': '12'}), required=False)
    category = forms.ChoiceField(choices=Product.PRODUCT_CATEGORY, widget=forms.Select(attrs={'class': 'form-select'}), required=False)
    usage = forms.ChoiceField(choices=Product.PRODUCT_USAGE, widget=forms.Select(attrs={'class': 'form-select'}), required=False)

    class Meta:
        model = Product
        fields = ['name', 'serial_number', 'category', 'usage', 'description']

class ShipmentForm(forms.ModelForm):
    # Add fields for quantity and product
    quantity = forms.IntegerField(label='Ποσότητα', required=True)
    products = forms.ModelChoiceField(queryset=Product.objects.all(), label='Προϊόντα', required=True)

    class Meta:
        model = Shipment
        fields = ['shipment_type', 'warehouse', 'recipient', 'notes', 'quantity', 'products']

    def __init__(self, *args, **kwargs):
        super(ShipmentForm, self).__init__(*args, **kwargs)
        # Customize widget attributes if needed
        self.fields['warehouse'].widget.attrs['class'] = 'form-select'
        self.fields['recipient'].widget.attrs['class'] = 'form-control'
        self.fields['notes'].widget.attrs['class'] = 'form-control'
        self.fields['quantity'].widget.attrs['class'] = 'form-control'
        self.fields['products'].widget.attrs['class'] = 'form-select'
