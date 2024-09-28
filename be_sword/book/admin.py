from django.contrib import admin
from django.contrib import messages
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import path

from book.forms import BookForm
from book.forms import UploadBooksForm
from book.models import Book
from book.models import BookReserve
from book.utils import handle_books_uploaded
from book.utils import send_invalid_file_email
from book.utils import send_uploaded_email


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["book_id", "title", "authors", "isbn13"]
    search_fields = ["book_id", "title", "authors", "isbn13"]
    form = BookForm

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        if not obj:
            last_book = Book.objects.order_by("book_id").last()
            next_book_id = last_book.book_id + 1 if last_book else 1
            form.base_fields["book_id"].initial = next_book_id

        return form

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
                try:
                    success, invalid_books = handle_books_uploaded(file)
                except KeyError:
                    self.message_user(request, "Invalid file format", messages.ERROR)
                    send_invalid_file_email()
                    return redirect("admin:book_book_changelist")
                self.message_user(
                    request, f"{success} books successfully added", messages.SUCCESS
                )
                if invalid_books:
                    self.message_user(
                        request,
                        f"Invalid books: {", ".join(invalid_books.keys())}",
                        messages.WARNING,
                    )
                send_uploaded_email(success, invalid_books)
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


@admin.register(BookReserve)
class BookReserveAdmin(admin.ModelAdmin):
    list_display = ["book", "reserve_date", "customer_name", "customer_email"]
    search_fields = ["book__title", "customer_name", "customer_email"]
