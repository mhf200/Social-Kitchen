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
    path ('MeatFilter', views.Meat_category_filter, name="Meat"),
    path ('ChickenFilter', views.Chicken_category_filter, name="Chicken"),
    path ('SaladsFilter', views.Salads_category_filter, name="Salads"),
    path ('SeaFoodFilter', views.SeaFood_category_filter, name="SeaFood"),
    path ('DrinksFilter', views.Drinks_category_filter, name="Drinks"),
    path ('SoupsFilter', views.Soups_category_filter, name="Soups"),
    path ('DessertsFilter', views.Desserts_category_filter, name="Desserts"),
    path ('OthersFilter', views.Others_category_filter, name="Others"),
    path('recipes/recommendations', views.recommendations, name='recommendations'),
    path('hislistings/', views.hislistings, name='hislistings'),


   
    


]