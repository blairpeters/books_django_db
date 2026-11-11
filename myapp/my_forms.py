from django import forms
from myapp.models import Book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'description','isdn','year','genre','price')