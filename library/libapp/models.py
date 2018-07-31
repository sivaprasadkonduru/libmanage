from django.db import models
from django.contrib.auth.models import AbstractUser

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

DEPARTMENTS = (("MBA", "Management"),
               ("MCA", "PG"),
               ("BTech","Bachelors"),
               ("MTech", "Masters"))

BRANCHES = (("ECE", "Electronics"),
            ("EEE", "Electrical"),
            ("CSE", "Computers"),
            ("CSIT", "Information Tech"),
            ("Civil", "Civil Engg"),
            )

GENDER = (("M", "Male"),
          ("F", "Female"))


class UserModel(AbstractUser):

    department = models.CharField(max_length=20, choices=DEPARTMENTS, default="BTech")
    branch = models.CharField(max_length=20, choices=BRANCHES, default="CSE")
    gender = models.CharField(max_length=10, choices=GENDER)
    rollno = models.CharField(max_length=20)
    doj = models.DateField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    phone_num = models.CharField(max_length=15)
    address = models.TextField(max_length=255, blank=True)


class Book(models.Model):
    book_user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='userbook')
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    category = models.CharField(choices=BOOK_CHOICES, max_length=100)
    publisher = models.CharField(max_length=50)
    availability = models.CharField(max_length=5, choices=AVAILABLE)
    edition = models.IntegerField()

    def __str__(self):
        return '-'.join([self.name, self.author, str(self.edition)])







