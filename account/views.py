from django.shortcuts import render, redirect
from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = RegisterForm()

    templ = "account/register.html"
    data = {"form": form}

    return render(request, templ, data)


def index(request):
    templ = 'base.html'
    return render(request, templ)