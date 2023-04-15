from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from .models import Ingredient

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class IngredientForm(forms.ModelForm):
    ingredient = forms.ModelChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Select an ingredient'
    )
    weight = forms.FloatField(
        initial=100,
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label='Weight (in grams)'
    )

    class Meta:
        model = Ingredient
        fields = ('ingredient', 'weight')