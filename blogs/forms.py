from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    title =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your title'}))
    content = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder':'Write something', 'rows':10,'col':5,}))
    active = forms.BooleanField()
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
        ]
