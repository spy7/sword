from django import forms


class UploadBooksForm(forms.Form):
    file = forms.FileField(help_text="Accepts .csv file")
