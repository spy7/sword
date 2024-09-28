from django import forms

from book.models import Book


class UploadBooksForm(forms.Form):
    file = forms.FileField(help_text="Accepts .csv file")


class BookForm(forms.ModelForm):
    image_url = forms.URLField(assume_scheme="http")
    small_image_url = forms.URLField(assume_scheme="http")

    class Meta:
        model = Book
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields["book_id"].widget.attrs["readonly"] = True
