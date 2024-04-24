from django import forms
from .models import Product, Shipment, ShipmentItem, Warehouse
from django.forms import inlineformset_factory

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
    batch_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Merida ilikou'}), required=False)
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'summernote', 'rows': '12'}), required=False)
    category = forms.ChoiceField(choices=Product.PRODUCT_CATEGORY, widget=forms.Select(attrs={'class': 'form-select'}), required=False)
    usage = forms.ChoiceField(choices=Product.PRODUCT_USAGE, widget=forms.Select(attrs={'class': 'form-select'}), required=False)
    unit_of_measurement = forms.ChoiceField(choices=Product.MEASUREMENT_TYPES, widget=forms.Select(attrs={'class': 'form-select'}), required=False)
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))  # Adding the image field

    class Meta:
        model = Product
        fields = ['name', 'batch_number', 'category', 'usage', 'description', 'unit_of_measurement', 'image']

# forms.py
class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['shipment_type', 'recipient', 'date',  'notes']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'shipment_type': forms.Select(attrs={'class': 'form-select', 'id': 'shipment_type_id'}),
            'recipient': forms.Select(attrs={'class': 'form-select', 'id': 'recipient_id'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(ShipmentForm, self).__init__(*args, **kwargs)
        # Hide the recipient field by default
        self.fields['recipient'].widget.attrs['style'] = 'display:none;'


class ShipmentItemForm(forms.ModelForm):
    class Meta:
        model = ShipmentItem
        fields = ['product', 'warehouse', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].widget.attrs.update({'class': 'form-select mb-2'})
        self.fields['warehouse'].queryset = Warehouse.objects.all()
        self.fields['warehouse'].widget.attrs.update({'class': 'form-select'})
        self.fields['warehouse'].empty_label = "Select Warehouse"
        self.fields['quantity'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ποσότητα'})
        
# Ensure to use ShipmentItemForm in the formset
ShipmentItemFormSet = inlineformset_factory(
    Shipment,
    ShipmentItem,
    form=ShipmentItemForm,  # Use the customized form
    fields=('product', 'warehouse', 'quantity'),
    extra=1,
    can_delete=True
)
