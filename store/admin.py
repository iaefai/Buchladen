from django.contrib import admin
from . import models

class BookAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'author_names', 'isbn', 'subject_list', 'publisher',
                     'price', 'date_added', 'user' )


admin.site.register(models.Author)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Subject)