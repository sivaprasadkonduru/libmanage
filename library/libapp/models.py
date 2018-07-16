from django.db import models

# Create your models here.

BOOK_CHOICES = (
    ('Electronics', 'ECE'),
    ('Electrical', 'EEE'),
    ('Civil', 'Civil'),
    ('Computers', 'CSE'),
    ('Mechanical', 'ME'),
    ('Management', 'MBA')
)

AVAILABLE = (
    ('YES', 'Y'),
    ('NO', 'N')
)


class Book(models.Model):

    name = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    category = models.CharField(choices=BOOK_CHOICES, max_length=100)
    publisher = models.CharField(max_length=50)
    availability = models.CharField(max_length=5, choices=AVAILABLE)
    edition = models.IntegerField()

    def __str__(self):
        return '-'.join([self.name, self.author, str(self.edition)])



