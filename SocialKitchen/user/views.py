from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate

def index(request):
    if request.method =="POST":
        form= UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your account have been created. login here")
            return redirect("login")
    
    else :

        form =UserRegistrationForm()

    return render(request, "user/register.html", {
        "form":form
        })