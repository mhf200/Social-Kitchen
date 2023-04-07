from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Recipe
from .models import Profile
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q

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

def index( request):
	return render(request, 'user/index.html')

def recipes(request):
    queryset = Recipe.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(Q(name__icontains=query))
        
    paginator = Paginator(queryset, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'recipes': page_obj
    }
    return render(request, 'user/index.html', context)

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
        ingredients = request.POST.get('ingredients')
        cooking_instructions = request.POST.get('cooking_instructions')
        image = request.FILES['upload']
        chef = request.user
        recipe = Recipe(name=name ,  desc=desc , ingredients=ingredients, cooking_instructions=cooking_instructions, image=image , chef=chef)
        recipe.save()
    return render(request, 'user/addrecipe.html')


def update_recipe(request , id ):
    recipe = Recipe.objects.get(id = id )
    if request.method == 'POST':
        recipe.name = request.POST.get('name')
        recipe.desc = request.POST.get('desc')
        recipe.ingredients = request.POST.get('ingredients')
        recipe.cooking_instructions = request.POST.get('cooking_instructions')
        if 'upload' in request.FILES:
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



@login_required
def create_profile(request):
     if request.method == 'POST':
          contact_number = request.POST.get('contact_number')
          image = request.FILES['upload']
          user = request.user
          profile = Profile(user=user , image=image , contact_number = contact_number)
          profile.save()
     return render(request,'user/createprofile.html')

def chef_profile(request,id):
     cheff = User.objects.get(id=id)
     context = {
          'cheff':cheff,
     }
     return render(request, 'user/chefprofile.html',context)
     
def my_listings(request):
     recipes = Recipe.objects.filter(chef=request.user)
     context = {
          'recipes':recipes,
     }
     return render(request, 'user/mylistings.html' , context)

def profile(request):
    users = User.objects.all()
    return render(request, 'user/users.html', {'users': users})


