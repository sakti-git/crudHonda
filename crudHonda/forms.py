from django import forms
from crudHonda.models import ProductModel


class ProductForms(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = "__all__"
