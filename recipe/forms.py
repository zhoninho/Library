from django import forms
from . import models

class RecipeForm(forms.ModelForm):
    class Meta:
        model = models.Recipe
        fields = '__all__'

class IngredientForm(forms.ModelForm):
    class Meta:
        model = models.Ingredient
        fields = '__all__'
