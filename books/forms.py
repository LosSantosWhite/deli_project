from django import forms
from django.forms.widgets import HiddenInput
from books.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name']

