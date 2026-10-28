
from django.shortcuts import render, get_object_or_404
from .models import Recipe, Category, Ingredient


def home(request):
    recipes = Recipe.objects.all()
    return render(request, "retsepapp/home.html", {
        "recipes": recipes
    })


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "retsepapp/recipe_list.html", {
        "recipes": recipes
    })


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, "retsepapp/recipe_detail.html", {
        "recipe": recipe
    })


def category_list(request):
    categories = Category.objects.all()
    return render(request, "retsepapp/category_list.html", {
        "categories": categories
    })


def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, "retsepapp/ingredient_list.html", {
        "ingredients": ingredients
    })
