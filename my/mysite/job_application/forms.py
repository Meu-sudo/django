from django import forms

class ApplicationForms(forms.Form):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    occupation = forms.CharField(max_length=80, initial="Unknown")
