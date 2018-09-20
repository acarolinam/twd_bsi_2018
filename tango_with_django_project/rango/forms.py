from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Informe o nome da Categoria: ")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)
