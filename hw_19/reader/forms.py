from django import forms

class ReaderForm(forms.Form):
    reader_name = forms.CharField(label="სახელი", max_length=50)
    reader_surname = forms.CharField(label="გვარი", max_length=50)
    reader_pn = forms.IntegerField(label="პნ")
