from django.urls import path
from . import views
urlpatterns = [
    path('recipes_list/', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipes_list/<int:id>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes_list/<int:id>/delete/', views.DeleteRecipeView.as_view(), name='delete_recipe'),
    path('add_recipe/', views.AddRecipeView.as_view(), name='add_recipe'),
    path('add_ingredient/', views.AddIngredientView.as_view(), name='add_ingredient'),
]
