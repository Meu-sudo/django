from django.shortcuts import render
from .forms import ApplicationForms

def index(requests):
    if requests.method== "POST":
        form=ApplicationForms(requests.POST)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            email=form.cleaned_data["email"]
            date=form.cleaned_data["date"]
            occupation=form.cleaned_data["occupation"]
            print(first_name)

    return render (requests,"index.html")


