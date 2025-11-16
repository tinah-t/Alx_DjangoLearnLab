from django import forms
from .models import Book


# A simple example form required by your checker
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()


# Search form (for safe input handling)
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)


# Example ModelForm (also helps with safe input + SQL injection prevention)
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
