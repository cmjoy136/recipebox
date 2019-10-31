from django.shortcuts import render
from recipebox.models import Author, Recipe

def index(request):
    html = "index.html"
    recipes = Recipe.objects.all()

    return render(request, html, {'data': recipes})

def author(request, author_id):
    html = "author.html"
    author = Author.objects.filter(id=author_id).first()
    recipes = Recipe.objects.filter(author=author_id)

    return render(request, html, {"data": author, 'recipes': recipes})

def recipe(request, recipe_id):
    html = 'recipe.html'
    recipe = Recipe.objects.filter(id=recipe_id).first()

    return render(request, html, {"data": recipe})



