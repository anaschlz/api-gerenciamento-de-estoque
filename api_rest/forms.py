from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        fields = ['product_id', 'product_name', 'product_amount', 'product_price']
