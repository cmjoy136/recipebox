from django.shortcuts import render, HttpResponseRedirect, reverse
from recipebox.models import Author, Recipe
from recipebox.forms import AuthorAddForm, RecipeEditForm
from recipebox.forms import RecipeAddForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.forms.models import model_to_dict
from django.contrib.admin.views.decorators import staff_member_required


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

# https://kite.com/python/docs/django.contrib.admindocs.views.staff_member_required


@staff_member_required
def authoraddview(request):
    html = "generic_form.html"
    form = AuthorAddForm()

    if request.method == 'POST':
        form = AuthorAddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data['name'],
                bio=data['bio']
            )

    return render(request, html, {'form': form})


def recipe_favorites(request, id):
    html = 'favorites.html'
    author = Author.objects.get(pk=id)
    favorites = author.favorites.all()

    return render(request, html, {'favorites': favorites, 'author': author})


def editrecipeview(request, id):
    html = 'generic_form.html'
    instance = Recipe.objects.get(id=id)
    form = RecipeEditForm(instance=instance)

    if request.method == "POST":
        form = RecipeEditForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()
            # this only works on a model form, for a simple form must access
            #  each attribute on instance i.e. instance.title=
            return HttpResponseRedirect(reverse('homepage'))

    return render(request, html, {'form': form})


@login_required
def recipeaddview(request):
    html = "generic_form.html"
    form = RecipeAddForm()
    if request.method == "POST":
        form = RecipeAddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                author=data["author"],
                title=data['title'],
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions']
            )
            return HttpResponseRedirect(reverse('homepage'))

    return render(request, html, {'form': form})


def login_view(request):
    html = "generic_form.html"
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', '/'))

    return render(request, html, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
