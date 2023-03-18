from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    Form =UserCreationForm
    if request.method=="post" :
        Form =UserCreationForm(request.post)
        if Form.is_valid():
            Form.save
            
    return render(request, "user/register.html", {
        "form":Form
    })