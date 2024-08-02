from django.contrib import admin

# Register your models here.
from books.models import Book, Author, BookAuthor, BookReview

class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'isbn')
    # list_filter = ('title',)

class AuthorAdmin(admin.ModelAdmin):
    pass

class BookAuthorAdmin(admin.ModelAdmin):
    pass

class BookReviewAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookAuthor, BookAuthorAdmin)
admin.site.register(BookReview, BookReviewAdmin)