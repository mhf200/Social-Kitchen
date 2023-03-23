from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Recipe
from .models import Profile

# Create your views here.

def loginPage(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password1']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' welcome {username} !!')
			return redirect('/recipes')
		else:
			messages.info(request, f'account does not exit plz sign in')
	form = CreateUserForm()
	return render(request, 'user/loginpage.html', {'form':form, 'title':'log in'})


def registerPage(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('user:home')
    else:
        form = CreateUserForm()
    return render(request, 'user/registerpage.html', {'form' : form})


@login_required
def logoutUser(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("user:home")

def home( request):
	return render(request, 'user/home.html')


def recipes(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes 
    }
    return render(request , 'user/index.html', context)

def recipe_detail(request,id):
    recipe = Recipe.objects.get(id=id)
    context = {
        'recipe':recipe 
    }
    return render(request , 'user/details.html ',context)


@login_required
def add_recipe(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        image = request.FILES['upload']
        chef = request.user
        recipe = Recipe(name=name ,  desc = desc , image=image , chef = chef)
        recipe.save()
    return render(request, 'user/addrecipe.html')

def update_recipe(request , id ):
    recipe = Recipe.objects.get(id = id )
    if request.method == 'POST':
        recipe.name = request.POST.get('name')
        recipe.desc = request.POST.get('desc')
        recipe.image = request.FILES['upload']
        recipe.save()
        return redirect('user:recipes')
    context = {
        'recipe':recipe,
    }
    return render(request , 'user/updaterecipe.html',context)

def delete_recipe(request,id):
    recipe = Recipe.objects.get(id = id )
    context = {
        'recipe':recipe,
    }

    if request.method == 'POST':
        recipe.delete()
        return redirect('user:recipes')
    return render(request,'user/delete.html',context)

def index(request):
    return render(request, 'user/index.html')



@login_required

def profile(request):
     return render(request, 'user/profile.html')

def create_profile(request):
     if request.method == 'POST':
          contact_number = request.POST.get('contact_number')
          image = request.FILES['upload']
          user = request.user
          profile = Profile(user=user , image=image , contact_number = contact_number)
          profile.save()
     return render(request,'user/createprofile.html')