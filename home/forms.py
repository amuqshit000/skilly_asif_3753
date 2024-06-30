from django import forms

class PdfToDocxForm(forms.Form):
    pdf_file = forms.FileField(label='Select a PDF file')


class ConvertForm(forms.Form):
    pdf_file = forms.FileField(label='Select a PDF file', help_text='max. 42 MB')

