from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
import xlrd
import os
from library.settings import BASE_DIR
from .models import Book
from .forms import BookForm
# Create your views here.
#excel_path = 'C:\\Users\\User\\workspace\\libmanage'


def book_data():
    file_name = 'C:\\Users\\User\\workspace\\libmanage\\books.xlsx'
    if os.path.exists(file_name):

        # Open the workbook
        xl_workbook = xlrd.open_workbook(file_name)
        sheet_names = xl_workbook.sheet_names()
        xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])
        #xl_sheet = xl_workbook.sheet_by_index(0)
        for row_idx in range(1, xl_sheet.nrows):
            data = xl_sheet.row_values(row_idx)
            b = Book.objects.get_or_create(name=data[0], author=data[1], category=data[2],
                        publisher=data[3], availability=data[4], edition=data[5])
    else:
        raise AttributeError("File path doesn't exist")


def get_books_data(request):

    book_data()
    data = Book.objects.all().order_by('edition')
    return render(request, 'book_details.html', {'book_data': data})


class BookView(ListView):
    template_name = 'book_details.html'
    model = Book
    queryset = Book.objects.all()
    ordering = '-edition'
    context_object_name = 'book_info'


def book_view(request):
    '''
    View which defines submitting data through modelform.
    :param request:
    :return: renders a form
    '''
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise form.ValidationErrors('Enter valid data.')

        return HttpResponseRedirect('/book/all_books/')

    else:
        form = BookForm()

    return render(request, 'book_form.html', {'form': form})


def create_book(request):
    '''
    View to define submitting data using form.
    :param request:
    :return: render form
    '''
    if request.method == 'POST':
        form = BookForm(request.POST)
        #import pdb;pdb.set_trace()
        if form.is_valid():
            data = form.cleaned_data
            Book.objects.create(name=data['name'], author=data['author'], category=data['category'],
                publisher=data['publisher'], availability=data['availability'], edition=data['edition'])
        else:
            raise form.ValidationErrors('Enter valid data.')

        return HttpResponseRedirect('/book/all_books/')

    else:
        form = BookForm()

    return render(request, 'book_form.html', {'form': form})






