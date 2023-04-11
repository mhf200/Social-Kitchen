from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Recipe(models.Model):
    def __str__(self):
        return self.name
    
    chef = models.ForeignKey(User,on_delete=models.CASCADE , default=1)    
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 200)
    ingredients = models.TextField()
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