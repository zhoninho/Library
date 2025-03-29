from django.shortcuts import render, get_object_or_404, redirect
from . import models
from . import forms
from django.views import generic

class RecipeListView(generic.ListView):
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'
    model = models.Recipe

class RecipeDetailView(generic.DetailView):
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'

    def get_object(self, *args, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(models.Recipe, id=recipe_id)

class AddRecipeView(generic.CreateView):
    template_name = 'recipes/add_recipe.html'
    form_class = forms.RecipeForm
    success_url = "/recipes_list/"

class AddIngredientView(generic.CreateView):
    template_name = 'recipes/add_ingredient.html'
    form_class = forms.IngredientForm
    success_url = "/recipes_list/"

class DeleteRecipeView(generic.DeleteView):
    template_name = 'recipes/confirm_delete.html'
    success_url = "/recipes_list/"

    def get_object(self, *args, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(models.Recipe, id=recipe_id)


