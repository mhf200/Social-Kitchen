from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm


def index(request):
    if request.method =="POST":
        form= UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else :

        form =UserRegistrationForm()

    return render(request, "user/register.html", {
        "form":form
        })