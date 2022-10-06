from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your title'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder':'Write something', 'rows':10,'col':5,}))
    price = forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not 'alex' in title:
            return forms.ValidationError('This is not a valid title')
        return title

class RawProductForm(forms.Form):
    title =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your title'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder':'Write something', 'rows':10,'col':5,}))
    price = forms.DecimalField(initial=199.99)