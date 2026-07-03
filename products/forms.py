from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'image','category']

    def clean_name(self):
        name = self.cleaned_data['name']
        if name[0] != name[0].upper():
            raise forms.ValidationError("First letter must be capital! Example: 'Iphone 15'")
        return name

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Price must be greater than 0!")
        return price

    def clean_stock(self):
        stock = self.cleaned_data['stock']
        if stock < 0:
            raise forms.ValidationError("Stock cannot be negative!")
        return stock