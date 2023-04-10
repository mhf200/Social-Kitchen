from django.urls import path
from . import views

app_name='user'

urlpatterns = [
    path('loginpage/', views.loginPage, name="loginpage"),
    path('registerpage/', views.registerPage, name="registerpage"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name='home'),
    path('recipes/',views.recipes , name='recipes') ,
    path ( 'recipes/<int:id>/', views.recipe_detail , name='recipe_detail' ),
    path('recipes/add', views.add_recipe, name='add_recipe'),
    path('recipes/update/<int:id>/' , views.update_recipe , name='update_recipe'),
    path('recipes/delete/<int:id>/' , views.delete_recipe , name='delete_recipe'),
   path('index', views.index, name='index'),
    path ('profile/',views.profile , name='profile'),
    path ('createprofile/',views.create_profile , name='createprofile'),
    path ('chefprofile/<int:id>',views.chef_profile , name='chefprofile'),
    path ('recipes/mylistings',views.my_listings , name='mylistings'),
    path ('recipes/myprofile',views.my_profile , name='myprofile'),
    path ('LeanMeatFilter', views.LeanMeat_category_filter, name="LeanMeat"),
    path ('WholeGrainsFilter', views.WholeGrains_category_filter, name="WholeGrains"),
    path ('VeganFilter', views.Vegan_category_filter, name="Vegan"),
    path ('DairyFilter', views.Dairy_category_filter, name="Dairy"),

]