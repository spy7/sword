from django.contrib import admin
from django.contrib import messages
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import path

from book.forms import UploadBooksForm
from book.models import Book
from book.utils import handle_books_uploaded
from book.utils import send_uploaded_email


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "authors", "isbn13"]
    search_fields = ["title", "authors", "isbn13"]

    def get_urls(self):
        urls = super().get_urls()
        return [
            path(
                "add-multiples-books/",
                self.admin_site.admin_view(self.add_multiples_books),
                name="add_multiples_books",
            )
        ] + urls

    def add_multiples_books(self, request):
        if request.method == "POST":
            form = UploadBooksForm(request.POST, request.FILES)
            if form.is_valid():
                file = form.cleaned_data["file"]
                invalid_books = handle_books_uploaded(file)
                self.message_user(request, "Books successfully added", messages.SUCCESS)
                if invalid_books:
                    self.message_user(
                        request, f"Invalid books: {invalid_books}", messages.WARNING
                    )
                send_uploaded_email(invalid_books)
                return redirect("admin:book_book_changelist")
        else:
            form = UploadBooksForm()
        context = dict(
            self.admin_site.each_context(request),
            form=form,
            title="Add Multiples Books",
            action="add",
        )
        return TemplateResponse(request, "admin/book/book/upload_file.html", context)
