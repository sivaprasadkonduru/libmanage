from django import forms
from .models import Book, BOOK_CHOICES, AVAILABLE


class BookForm(forms.Form):

    name = forms.CharField(max_length=50, label='Book Name')
    author = forms.CharField(max_length=50, label='Author')
    category = forms.ChoiceField(choices=BOOK_CHOICES, label='Category')
    publisher = forms.CharField(max_length=50, initial='Orielly')
    availability = forms.ChoiceField(choices=AVAILABLE, label='Availability')
    edition = forms.IntegerField(label='Edition')


'''class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        #fields = ('name', 'author', 'edition')
        fields = '__all__'
        #exclude = ('')'''
