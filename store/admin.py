from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from . import models

class BookAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'author_names', 'isbn', 'subject_list', 'publisher',
                     'price', 'date_added', 'user' )

class CustomerInline(admin.StackedInline):
    model = models.Customer
    can_delete = False
    verbose_name_plural = "customers"

class UserAdmin(UserAdmin):
    inlines = (CustomerInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(models.Author)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Subject)