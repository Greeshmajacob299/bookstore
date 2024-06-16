from django import forms
from .models import Book1,Author


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['name']

class Book1Form(forms.ModelForm):

    class Meta:
        model = Book1
        fields = '__all__'


        widgets={
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'enter the book name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'enter the book price'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'enter the author'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'enter the book quantity'})

        }

