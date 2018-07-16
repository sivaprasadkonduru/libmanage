from django.shortcuts import render
from django.http import HttpResponse
import xlrd
import os
from library.settings import BASE_DIR
from .models import Book
# Create your views here.
#excel_path = 'C:\\Users\\User\\workspace\\libmanage'


def book_data(request):
    file_name = 'C:\\Users\\User\\workspace\\libmanage\\books.xlsx'
    if os.path.exists(file_name):

        # Open the workbook
        xl_workbook = xlrd.open_workbook(file_name)
        sheet_names = xl_workbook.sheet_names()

        #print('Sheet Names', sheet_names)
        xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])
        #import pdb; pdb.set_trace()
        for row_idx in range(1, xl_sheet.nrows):

            data = xl_sheet.row_values(row_idx)
            b = Book(name=data[0], author=data[1], category=data[2],
                     publisher=data[3], availability=data[4], edition=data[5])
            b.save()

        return HttpResponse(dir(xl_sheet))
