from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
# Create your models here.

class Ingredient(models.Model):
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=100)
    calories = models.FloatField(default=0, validators=[MinValueValidator(0)])
    protein = models.FloatField(default=0, validators=[MinValueValidator(0)])
    carbohydrates = models.FloatField(default=0, validators=[MinValueValidator(0)])
    fats = models.FloatField(default=0, validators=[MinValueValidator(0)])
    weight = models.FloatField(default=100, validators=[MinValueValidator(0)])

class Recipe(models.Model):
    def __str__(self):
        return self.name
    
    chef = models.ForeignKey(User,on_delete=models.CASCADE , default=1)    
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 200)
    ingredients = models.ManyToManyField(Ingredient)
    cooking_instructions = models.TextField()
    image = models.ImageField(blank=True,upload_to='images')
    category = models.CharField(max_length=100, default='uncategorized')


class Profile (models.Model):
    def __str__(self):
        return self.user.username
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile.jpg',upload_to='profile_pictures')
    contact_number = models.CharField(max_length=100,default='999')


class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

