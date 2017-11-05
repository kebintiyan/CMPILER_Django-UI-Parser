from django import forms

class ParseForm(forms.Form):
    file = forms.FileField()
