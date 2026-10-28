
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("recipes/", views.recipe_list, name="recipe_list"),
    path("recipes/<int:pk>/", views.recipe_detail, name="recipe_detail"),
    path("categories/", views.category_list, name="category_list"),
    path("ingredients/", views.ingredient_list, name="ingredient_list"),
]
