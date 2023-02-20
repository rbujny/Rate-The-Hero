from django import forms
from .models import Review

class ReviewForm(forms.Form):
    rating = forms.IntegerField(min_value=1, max_value=10)
    text = forms.CharField(widget=forms.Textarea(), min_length=200)

class SearchForm(forms.Form):
    name = forms.CharField(max_length=200,
                           widget=forms.TextInput(attrs={'placeholder': 'Enter hero name'}))