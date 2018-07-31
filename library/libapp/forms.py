from django import forms
from .models import Book, BOOK_CHOICES, AVAILABLE, UserModel


'''class BookForm(forms.Form):
    #book_user = 
    name = forms.CharField(max_length=50, label='Book Name')
    author = forms.CharField(max_length=50, label='Author')
    category = forms.ChoiceField(choices=BOOK_CHOICES, label='Category')
    publisher = forms.CharField(max_length=50, initial='Orielly')
    availability = forms.ChoiceField(choices=AVAILABLE, label='Availability')
    edition = forms.IntegerField(label='Edition')
'''

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        #fields = ('name', 'author', 'edition')
        fields = '__all__'
        #exclude = ('')


class SignUpForm(forms.ModelForm):

    username = forms.CharField(max_length=30, required=True, label="UserName")
    email = forms.EmailField(max_length=255, required=True, label="Email")
    first_name = forms.CharField(max_length=30, required=True, label='FirstName')
    last_name = forms.CharField(max_length=30, required=True, label='LastName')
    password = forms.CharField(max_length=30, required=True, label='Password', widget=forms.PasswordInput())

    class Meta:

        model = UserModel
        fields = ('department', 'branch', 'gender', 'rollno', 'doj', 'dob', 'phone_num', 'address')
        #fields = '__all__'
