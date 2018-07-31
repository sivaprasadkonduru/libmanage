from django.contrib import admin
from .models import Book, UserModel
# Register your models here.


class DjUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserModel, DjUserAdmin)
admin.site.register(Book)
