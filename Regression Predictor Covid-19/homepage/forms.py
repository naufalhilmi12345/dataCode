from django import forms

class dateForm(forms.Form):
    tanggal = forms.DateField(widget=forms.DateInput(attrs={
        "class" : "form-control",
        "type" : "date",
        "required" : True
    }))