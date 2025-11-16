from django import forms
from .models import Book

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)


# Example form for adding a Book (optional but useful)
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author"]
